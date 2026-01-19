<#
.SYNOPSIS
    Verifica o status básico do sistema Windows (Disco, Serviços Críticos, Informações do SO).
.DESCRIPTION
    Este script coleta informações sobre espaço em disco livre, status de serviços importantes e informações básicas do sistema operacional.
#>

Write-Host "=== Verificação de Status do Windows ===" -ForegroundColor Cyan
Get-Date
Write-Host ""

# 1. Verificar Espaço em Disco
Write-Host "--- Espaço em Disco ---" -ForegroundColor Yellow
$disks = Get-LogicalDisk -DriveType 3
foreach ($disk in $disks) {
    $percentFree = ($disk.FreeSpace / $disk.Size) * 100
    $formattedPercent = "{0:N2}" -f $percentFree
    
    if ($percentFree -lt 10) {
        Write-Host "CRÍTICO: Unidade $($disk.DeviceID) tem apenas $formattedPercent% livre!" -ForegroundColor Red
    } elseif ($percentFree -lt 20) {
        Write-Host "ALERTA: Unidade $($disk.DeviceID) tem $formattedPercent% livre." -ForegroundColor Yellow
    } else {
        Write-Host "OK: Unidade $($disk.DeviceID) tem $formattedPercent% livre." -ForegroundColor Green
    }
}
Write-Host ""

# 2. Informações do Sistema
Write-Host "--- Informações do Sistema ---" -ForegroundColor Yellow
$os = Get-CimInstance Win32_OperatingSystem
Write-Host "SO: $($os.Caption)"
Write-Host "Versão: $($os.Version)"
Write-Host "Memória Total: $([Math]::Round($os.TotalVisibleMemorySize / 1MB, 2)) GB"
Write-Host "Memória Livre: $([Math]::Round($os.FreePhysicalMemory / 1MB, 2)) GB"
Write-Host "Último Boot: $($os.LastBootUpTime)"
Write-Host ""

# 3. Teste de Rede Simples
Write-Host "--- Conectividade ---" -ForegroundColor Yellow
$google = Test-Connection -ComputerName 8.8.8.8 -Count 1 -Quiet
if ($google) {
    Write-Host "Internet (Google DNS): Conectado" -ForegroundColor Green
} else {
    Write-Host "Internet (Google DNS): Falha na conexão" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Fim da Verificação ===" -ForegroundColor Cyan
