<#
.SYNOPSIS
    Limpa arquivos temporários do usuário.
.DESCRIPTION
    Remove arquivos da pasta %TEMP% que não estão em uso.
#>

Write-Host "Iniciando limpeza de arquivos temporários..." -ForegroundColor Cyan

$tempPath = [System.IO.Path]::GetTempPath()
Write-Host "Pasta Temp: $tempPath"

$files = Get-ChildItem -Path $tempPath -Recurse -Force -ErrorAction SilentlyContinue
$deletedCount = 0
$sizeFreed = 0

foreach ($file in $files) {
    try {
        # Tenta deletar o arquivo/pasta
        Remove-Item -Path $file.FullName -Force -Recurse -ErrorAction Stop
        $deletedCount++
        if (-not $file.PSIsContainer) {
            $sizeFreed += $file.Length
        }
        Write-Verbose "Deletado: $($file.Name)"
    }
    catch {
        # Ignora arquivos em uso
        Write-Verbose "Falha ao deletar: $($file.Name) (provavelmente em uso)"
    }
}

$sizeFreedMB = [Math]::Round($sizeFreed / 1MB, 2)
Write-Host "Limpeza concluída!" -ForegroundColor Green
Write-Host "Itens removidos: $deletedCount"
Write-Host "Espaço liberado (aprox): $sizeFreedMB MB"
