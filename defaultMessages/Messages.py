
class Messages:

        def getText_start(self) -> str:
                text_start = """
<strong>             ஜ🌹  ʙɪʙʟɪᴏᴛᴇᴄᴀ ᴅᴇ ʟɪᴠʀᴏs sᴀ́ғɪᴄᴏs  🌹ஜ</strong>


➲<strong>🌥 ʟɪsᴛᴀʀ ʟɪᴠʀᴏs ᴘᴏʀ:
                               
        •📂 /cat - ᴄᴀᴛᴇɢᴏʀɪᴀs

        •👩‍💼 /aut - ᴀᴜᴛᴏʀᴇs </strong>  



<i>Você também pode:</i>
<i>🔎 /pesquisar - Para pesquisar um livro pelo nome, 
digite "/pesquisar + nome do livro" a qualquer momento.</i>
<i>📨 /enviar - Envie um livro da biblioteca ou qualquer 
outro arquivo externo para seu kindle.</i>


Source code: https://github.com/xsatellit/BookLibrary
"""
                return text_start
        
        
        
        def getText_sendFiles(self, name: str) -> str:
                text_sendFiles = f"""💻  Olá <strong>{name}</strong>, 
Há duas opções de envio para o kindle:
- Interno (arquivos dentro da biblioteca)
- Externos (seus próprios arquivos)

Para enviar um arquivo da biblioteca, você pode pesquisá-lo, digitando /pesquisar + nome do livro ou clicar em "ENVIAR PARA KINDLE" ao selecionar um dos arquivos dentro da biblioteca.

Se você deseja enviar um arquivo externo, digite </strong>/enviar meu arquivo</strong> e siga as instruções.

❗ E-mail do bot para adicionar na lista de e-mails aprovados: <strong>bibliotecabotlesb@gmail.com</strong>"""
                return text_sendFiles
        
        
        
        def getText_kindle_tips(self) -> str:
                text_kindle_tips = '''Dicas <strong>necessárias</strong> para anexos de documentos pessoais:

❗ O Serviço de documentos pessoais do Kindle pode converter e entregar os seguintes tipos de documentos:
<strong>- Microsoft Word (.doc, .docx) 
- Formato Rich Text (.rtf) 
- HTML (.htm, .html) 
- Documentos de texto (.txt) 
- Documentos arquivados (zip, x-zip) e documentos compactados
- MOBI (.azw, .mobi) (não suporta os recursos mais novos do Kindle para documentos)
- EPUB (.epub)
- Formato Adobe PDF (.pdf)
- Imagens que são do tipo JPEGs (.jpg), GIFs (.gif), Bitmaps (.bmp), e imagens PNG (.png).</strong>

❗ O tamanho do arquivo de cada documento pessoal anexado deve ser inferior a 50 MB/50.000 KB (antes da compactação em um arquivo ZIP).

❗ Por ora, só é possível fazer envio de um arquivo por vez, portanto para cada arquivo a ser enviado é necessário digitar o comando /enviar meu arquivo.'''
                return text_kindle_tips


        def getText_book(self, synopsis: str, author: str, bookName: str) -> str:
                text_book = f'''🌈  <i>Nome do livro:  <strong>{bookName}</strong>  </i>

👩‍💼  <i>Autora:  <strong>{author}</strong></i>


📃  <strong>Sinopse</strong>: 


{synopsis}
'''
                return text_book

        def getEmail_text(self, name: str) -> str:
                text_email = f'''🤖 Olá {name}, vamos cadastrar seu email, o processo é simples, mas para evitar mal-entendidos, precisamos esclarecer algumas coisas:

1. O email que será cadastrado será o email <strong>kindle</strong> e <strong>não seu email pessoal</strong>. Caso não saiba seu email kindle, <a href='https://ajuda.clippingcacd.com.br/pt-BR/articles/1217677-como-descobrir-qual-e-meu-e-mail-no-kindle'>clique aqui</a>.

2. Você pode cancelar o cadastro a qualquer momento.

3. Se por eventuais problemas você deseje alterar ou excluir seu email, digite /email e siga as instruções.

Agora:'''

                return text_email

        def getText_AdmPanel(self, name: str, role: str) -> str:

                text_adm = f"""<strong>PAINEL DE CONTROLE</strong>

👩🏻‍💻 Olá {name}! Seu cargo atual é: <strong>{role}</strong>.


Selecione uma opção abaixo para começar:
"""
                return text_adm

        def getText_AddBook() -> str:
                text_book = """Antes de iniciar o processo de adicionar um livro à biblioteca, é importante conhecer alguns detalhes:


⚠️ 1. Serão questionadas informações fundamentais sobre o livro: nome, autor(a), gênero (Aventura, Biografia, Drama, Fantasia, Ficção Científica ou Romance) e sinopse. Após fornecer essas informações, uma amostra do livro será exibida para que você possa visualizá-lo na biblioteca. Se notar algum erro ou inconsistência, é possível cancelar o processo e começar novamente. É importante lembrar que a precisão das informações é <strong>fundamental para que os leitores possam encontrar o livro com facilidade e entender do que se trata a obra. Portanto, forneça todas as informações com cuidado e atenção aos detalhes.</strong>

⚠️ 2. Esteja com os <strong>três</strong> tipos de arquivos preparados: pdf, epub e mobi. Caso algum esteja em falta, não será possível adicionar o livro. 

⚠️ 3. <strong>Revise os arquivos antes de enviá-los</strong>. É possivel substituí-los posteriormente, porém remover e adicionar arquivos locais demandam muito mais processamento do servidor do que o apropriado, podendo até interromper a conexão entre o telegram e o bot.

⚠️ 4. Os arquivos precisam seguir um modelo padrão para facilitar sua busca quando necessário. O modelo a seguir é: Nome do Livro - Autor. Exemplo: O preço do sal - Patricia Highsmith \nCaso haja mais do que um autor, separe-os por uma vírgula. Não use pontos finais. 

⚠️ 4. É possível cancelar o procedimento a qualquer momento. O comando é simples: digite <strong>cancelar</strong>.
"""
                return text_book