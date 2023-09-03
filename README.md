# SMTP

Assingment for Computer Networking course, which objective was to create a simplified prototype of a email server (SMTP) using sockets.

Instructions to executate/compile (in Portuguese):
 
1- Abrir o código servidor no linha de comando junto do nome do arquivo de lista de usuarios (lista_usuarios).<br>
2- Abrir o código do cliente no vscode (pode ser em outra IDE/editor de texto).<br>
3- Comandos do programa usuário (seguir a ordem):<br>
		&nbsp;&nbsp;1- "HELO" + domínio do email (exemplo: bol.com.br)<br>
        &nbsp;&nbsp;2- "MAIL FROM:" + email do remetente (exemplo: cicrano@bol.com.br) <br> 
        &nbsp;&nbsp;3- "RCPT TO:" + email do remetente (exemplo: fulano1@bol.com.br)<br>
        &nbsp;&nbsp;4- "DATA"   <br>
        &nbsp;&nbsp;5- Dados do email, terminar com "." sozinho em uma nova linha<br>
        &nbsp;&nbsp;6- Voltar para o passo 3 caso queira mandar mais mensagens<br>
        &nbsp;&nbsp;* "QUIT" pode ser usado em qualquer momento da execução para terminar a conexão do usuário com o servidor <br>
        &nbsp;&nbsp;** Depois de usar "QUIT" o servidor vai começar outra conexão, então voltar ao passo 1
