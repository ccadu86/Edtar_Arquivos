| Parâmetro | Funcionamento |
|-----------|---------------|
| "r"       | Modo de leitura. Abre o arquivo para leitura (padrão). |
| "w"       | Modo de escrita. Abre o arquivo para escrita, criando um novo arquivo se ele não existir. Se o arquivo já existir, seu conteúdo será sobrescrito. |
| "a"       | Modo de anexação. Abre o arquivo para escrita, mas adiciona novos dados ao final do arquivo, se ele já existir, em vez de sobrescrevê-lo. Se o arquivo não existir, ele será criado. |
| "x"       | Modo de criação. Abre o arquivo para escrita, mas gera um erro se o arquivo já existir. |
| "b"       | Modo binário. Abre o arquivo em modo binário, permitindo a leitura ou escrita de dados binários. Por exemplo, "rb" para leitura binária e "wb" para escrita binária. |
| "t"       | Modo de texto (padrão). Abre o arquivo em modo de texto, permitindo a leitura ou escrita de strings. Por exemplo, "rt" para leitura de texto e "wt" para escrita de texto. |
| "+"       | Modo de atualização. Permite a leitura e escrita no mesmo arquivo. Por exemplo, "r+" para leitura e escrita, "w+" para escrita e leitura, "a+" para anexação e leitura. |
| "U"       | Modo universal de nova linha. Modo especial que transforma automaticamente todas as diferentes convenções de nova linha em "\n" ao ler. Este modo não é mais necessário em Python 3.x. |
| "encoding" | Especifica a codificação de caracteres a ser usada ao ler ou escrever o arquivo. Por exemplo, "utf-8" ou "latin-1". |