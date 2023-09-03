def count_and_replace_words(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
        count = content.count('terrible')
    
    replaced_content = content
    replaced_count = 0
    
    index = 0
    while index != -1:
        index = replaced_content.find('terrible', index)
        if index != -1:
            if replaced_count % 2 == 0:
                replaced_content = replaced_content[:index] + 'marvellous' + replaced_content[index + len('terrible'):]
            else:
                replaced_content = replaced_content[:index] + 'pathetic' + replaced_content[index + len('terrible'):]
            index += len('marvellous')
            replaced_count += 1
    
    with open(output_file, 'w') as file:
        file.write(replaced_content)
    
    return count

input_file = 'file_to_read.txt'
output_file = 'file_to_write.txt'

word_count = count_and_replace_words(input_file, output_file)
print(f"单词'terrible'出现的总次数为：{word_count}")
