
import os


def interesting_moments():
    from openai import OpenAI
    with open(r'C:\Users\eWwic0rn\Documents\python\auto-shorts\projects\test2\temp\test2.srt', 'r', encoding='utf-8') as file:
        full_text = file.readlines()
    
    for i in range(0, len(full_text)):
        line = full_text[i].strip()



    client = OpenAI(
            base_url="http://localhost:1234/v1",
            api_key="lm-studio"
        )

    response = client.chat.completions.create(
                    model="qwen2.5-7b-instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": """Ты — профессиональный редактор вирусных YouTube Shorts и эксперт по удержанию внимания.

                            Тебе даётся ФРАГМЕНТ субтитров видео в формате SRT.
                            Это НЕ весь ролик, а только его часть.

                            Твоя задача — найти НЕ БОЛЕЕ ДВУХ фрагментов, которые:
                            - максимально цепляют внимание зрителя
                            - подходят для YouTube Shorts
                            - могут заставить зрителя досмотреть ролик до конца

                            СТРОГИЕ ТРЕБОВАНИЯ К ФРАГМЕНТУ:
                            - длительность от 25 до 60 секунд
                            - начинается с законченной мысли или целого предложения
                            - если в тексте есть вопрос, ответ ОБЯЗАН входить в выбранный фрагмент
                            - фрагмент должен быть ОДНИМ ЦЕЛЫМ куском, без разрывов
                            - фрагмент должен быть эмоционально, конфликтно или смыслово сильным

                            ТЫ ДОЛЖЕН ВЫВЕСТИ ТОЛЬКО JSON.
                            НИКАКОГО ТЕКСТА, ПОЯСНЕНИЙ, КОММЕНТАРИЕВ.

                            ФОРМАТ ВЫВОДА СТРОГО ТАКОЙ:

                            {
                            "moments": [
                                {
                                "start": "HH:MM:SS,mmm",
                                "end": "HH:MM:SS,mmm",
                                "title": "кликбейтное название, вызывающее желание кликнуть"
                                }
                            ]
                            }

                            ПРАВИЛА:
                            - если подходящих моментов НЕТ — верни { "moments": [] }
                            - не выдумывай таймкоды
                            - не выходи за границы предоставленного текста
                            - не повторяй один и тот же момент дважды
                            - названия должны быть КЛИКБЕЙТНЫМИ, но без вранья
                            """
                        },
                        {
                            "role": "user",
                            "content": script
                        }
                    ],
                )
    return response.choices[0].message.content

print(interesting_moments())