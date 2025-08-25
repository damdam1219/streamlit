# 가상환경 venv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델과 토크나이저 로드
model_name = "dlckdfuf141/korean-emotion-kluebert-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 감정 라벨 확인
labels = model.config.id2label
print(labels)  # 예: {0: 'happy', 1: 'sad', 2: 'angry', ...}

def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred_label = torch.argmax(probs, dim=1).item()
    pred_emotion = labels[pred_label]
    confidence = probs[0][pred_label].item()
    return pred_emotion, confidence

# 테스트
text = "오늘 상사한테 너무 깨졌어 어떻게 하면 나을까?"
emotion, score = predict_emotion(text)
print(emotion, score)

prompt = f"""
너는 친절하고 경험 많은 심리상담사야. 
사용자가 지금 느끼는 감정과 상태를 이해하고 공감해주면서 대화해야 해.
사용자가 입력한 문장: "{text}"
사용자 감정 분석 결과: {emotion}  
(신뢰도: {score:.2f})

- 먼저 사용자의 감정을 충분히 공감하고 이해를 표현해줘.
- 그 다음, 상황을 개선할 수 있는 현실적 조언이나 방법을 2~3가지 제안해줘.
- 만약 감정 분석의 정확도가 낮아 보이면, "혹시 이런 감정이 맞나요?" 처럼 되묻는 방식으로 자연스럽게 대화를 이어가.
- 말투는 친근하고 따뜻하게, 마치 실제 상담사가 상담하는 것처럼 작성해줘.
"""

from openai import OpenAI

client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

advice = response.choices[0].message.content
print(advice)

