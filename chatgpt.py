import os
import openai
import sys
import time

openai.api_key = " YourAPI"

message = "你是一个专业中文翻英文的翻译员，在翻译过程中请遵循下面的遵循原则:\n1. 严格遵循目标语言的语法和词汇使用规范，不得随意添加、删除或调整语言表达；\n2. 在翻译中保持原文的意思和语气，尽可能不改变作者的原意；\n3. 注重上下文的整体理解和把握，确保翻译完整、连贯、通顺；\n4. 在翻译中注重语言风格和本土化，结合目标读者的文化背景和语言习惯，以便让翻译文本更加自然流畅；\n"
#message = "You are a professional translator specialized in translating Chinese to English. During the translation process, please follow the following principles:\n1. Strictly adhere to the grammar and vocabulary usage norms of the target language, and do not add, delete or adjust the language expression at will;\n2. Maintain the meaning and tone of the original text in the translation, and try not to change the author's original intention;\n3. Pay attention to the overall understanding and grasp of the context to ensure that the translation is complete, coherent and fluent;\n4. Pay attention to language style and localization in the translation, combined with the cultural background and language habits of the target readers, in order to make the translated text more natural and fluent."

src_file = sys.argv[1]
ref_file = sys.argv[2]
out_file = sys.argv[3]

with open(src_file, "r", encoding="utf-8") as src_f,\
    open(ref_file, "r", encoding="utf-8") as ref_f,\
    open(out_file, "w", encoding="utf-8") as out_f:
    for src_line, ref_line in zip(src_f, ref_f):
        prompt = "下面有一句较难翻译的 中文句子:\n{}假如这句中文对应的可能的英文翻译如下:\n{}请结合上面的五条翻译原则，给出与上述译文有所区别但高质量的 10 条英文译文，质量由高到低，每行一条译文".format(src_line, ref_line)
        #prompt = "The following is a difficult-to-translate Chinese sentence:\n{}If a possible English translation corresponding to the Chinese sentence is as follows:\n{}Please provide 2 high-quality English translations that differ from the above translation but adhere to the five principles of translation listed above, with the highest quality at the top and the lowest at the bottom, and one translation per line.".format(src_line, ref_line)
        print(prompt)

        while True:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": message},
                        {"role": "user", "content": prompt},
                    ],
                )
                break
            except Exception as e:
                print(e)
                print("Retry in 10 seconds")
                time.sleep(10)
    
        response = response["choices"][0]["message"]["content"]
        print(response, "\n")
        out_f.write(response + "\n")
    

