# chapters_parser
Как коммуниздить главы с рулейта в случае запрета автора на скачивание и копирование и не попасть под наблюдение санитаров?
Внимание! Я не приветствую пиратство и свободное бесплатное распространение литературы современных авторов! Они старались и им надо что-то кушать!
Данная программа способна собирать текст, доступный вам, то есть, будьте добры, купите главы.

Итак, схема такова:
1. Скачиваете в отдельную папку html страницы с главой, где виден текст главы (правой кнопкой клац по шапке или ctrl+S и сохраняете страницу ПОЛНОСТЬЮ)
2. При переходе на каждую следующую главу обновляйте страницу, иначе скачаете предыдущую.
3. Создаете папку, куда будете сохранять тексты глав.
4. В переменную pyth_html_dir прописываете путь к папке с html страницами.
5. В переменную pyth_text_dir прописываете путь к папке с текстами.
6. Запускаете parser_chapters() - получаете тексты.
7. Запускаете fb2_writer() - получаете файл с fb2 разметкой и записанными главами. В переменной pretext внутри fb2_writer() поменяйте название, имя фамилию автора и описание там, где нужно.
8. Сменой типа файла получившийся файл можно поменять на fb2.