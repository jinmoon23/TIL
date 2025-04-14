import OpenDartReader

api_key = '591c0fdcd4ca790a4b5c3ab0fd36633d325127ca'

dart = OpenDartReader(api_key)

dart_list = dart.list('064400', start='2024-01-01', kind='A', final=False)

current_report = dart_list['rcept_no'][0]

print(current_report)

xml_text = dart.document(current_report)

import re # 전처리 함수

def extract_refine_text(html_string):
    # Remove CSS styles
    no_css = re.sub('<style.*?</style>', '', html_string, flags=re.DOTALL)

    # Remove Inline CSS
    no_inline_css = re.sub('\..*?{.*?}', '', no_css, flags=re.DOTALL)

    # Remove specific undesired strings
    no_undesired = re.sub('\d{4}[A-Za-z0-9_]*" ADELETETABLE="N">', '', no_inline_css)

    # Remove HTML tags
    no_tags = re.sub('<[^>]+>', ' ', no_undesired)

    # Remove special characters and whitespaces
    cleaned = re.sub('\s+', ' ', no_tags).strip()

    # Remove the □ character
    no_square = re.sub('□', '', cleaned)

    # Replace \' with '
    final_text = re.sub(r"\\'", "'", no_square)

    return final_text


refined_text = extract_refine_text(xml_text)
print(refined_text) # 텍스트 전처리 여부 확인



with open(f"마음AI_{current_report}.txt", 'w', encoding='utf-8') as f:
          f.write(refined_text) # 텍스트 파일 저장

