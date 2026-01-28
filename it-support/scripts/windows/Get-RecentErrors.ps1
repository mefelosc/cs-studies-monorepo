<#
.SYNOPSIS
    Lista os erros mais recentes dos logs de eventos do Windows.
.DESCRIPTION
    Este script recupera os últimos 10 erros dos logs de 'System' e 'Application', 
    ajudando a identificar falhas recentes no sistema ou aplicativos.
#>

Write-Host "=== Últimos Erros do Log de Eventos ===" -ForegroundColor Cyan
Get-Date
Write-Host ""

try {
    $systemErrors = Get-EventLog -LogName System -EntryType Error -Newest 5 -ErrorAction SilentlyContinue
    $appErrors = Get-EventLog -LogName Application -EntryType Error -Newest 5 -ErrorAction SilentlyContinue

    $allErrors = $systemErrors + $appErrors | Sort-Object TimeGenerated -Descending | Select-Object -First 10

    if ($allErrors) {
        $allErrors | Format-Table -AutoSize -Property TimeGenerated, Source, EventID, Message
    } else {
        Write-Host "Nenhum erro recente encontrado nos principais logs." -ForegroundColor Green
    }
} catch {
    Write-Host "Ocorreu um erro ao consultar os logs de eventos: $_" -ForegroundColor Red
}
