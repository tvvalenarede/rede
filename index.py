<html>
<head>
    <meta charset="UTF-8">
    <title>TVVALENAREDE - Contato</title>
    <style>
        body {
            background-color: #FFA500; /* Fundo laranja */
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
        }

        .rede-social {
            text-align: center;
            margin-bottom: 30px;
        }

        .titulo-rede {
            font-size: 2.5em;
            color: #000;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
            margin: 20px 0;
        }

        .botoes-rede {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            max-width: 800px;
            margin: 0 auto;
        }

        .botao-social {
            padding: 15px;
            background-color: #FF8C00;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: transform 0.3s;
        }

        .botao-social:hover {
            transform: scale(1.05);
            background-color: #FF6B00;
        }

        form {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            max-width: 500px;
            margin: 30px auto;
        }

        label, input, textarea {
            display: block;
            width: 100%;
            margin-bottom: 15px;
        }

        button[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <div class="rede-social">
        <h1 class="titulo-rede">REDE SOCIAL TVVALENAREDE</h1>
        <div class="botoes-rede">
            <a href="https://tvvalenarede0.webnode.page/?_gl=1*gzjijo*_gcl_au*MTI0NjU5NzMzNS4xNzQxNzI2MjQ1" class="botao-social"> ACESSE MADE CENTER</a>
            <a href="http://www.youtube.com/tvvalenarede" class="botao-social"> ACESSE SERGIUS ALIANÇAS</a>
            <a href="http://www.youtube.com/tvvalenarede" class="botao-social">ACESSE BAR DO OSMAR</a>
            <a href="http://www.youtube.com/tvvalenarede" class="botao-social">ACESSE CASA IRMÃOS</a>
            <a href="http://www.youtube.com/tvvalenarede" class="botao-social">ACESSE J.E.C.S</a>
            <a href="http://www.youtube.com/tvvalenarede" class="botao-social">ACESSE SERGINHO PNEUS</a>
            
            
        </div>
    </div>

    <form id="meuFormulario" action="https://formsubmit.co/tvrbrazil@gmail.com" method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="Nome" required>

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="E-mail" required>

        <label for="mensagem">Mensagem:</label>
        <textarea id="mensagem" name="Mensagem" rows="5" required></textarea>

        <input type="hidden" name="_subject" value="Nova submissão do site">
        
        <button type="submit">Enviar Mensagem</button>
    </form>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const formulario = document.getElementById('meuFormulario');

            formulario.addEventListener('submit', (e) => {
                e.preventDefault();

                // Validação do e-mail
                const email = formulario.email.value;
                if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    alert('Por favor, insira um e-mail válido!');
                    return;
                }

                // Validação da mensagem
                if (formulario.mensagem.value.trim().length < 10) {
                    alert('A mensagem deve ter pelo menos 10 caracteres!');
                    return;
                }

                // Confirmação de envio
                if (confirm('Deseja realmente enviar a mensagem?')) {
                    formulario.submit();
                    alert('Mensagem enviada com sucesso!');
                    formulario.reset();
                }
            });
        });
    </script>
</body>
</html>
