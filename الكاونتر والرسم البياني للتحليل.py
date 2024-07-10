#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Initialize counters
correct_answers = 0
incorrect_answers = 0

# Generate and present similar equations 
similar_equations = generate_similar_equations(train_expression) 
for eq in similar_equations: 
    print(f"معادلة مشابهة: {eq}") 
    text_to_speech(f"معادلة مشابهة: {eq}") 
     
    # الحصول على إجابة المستخدم 
    user_answer = get_audio() 
    if user_answer: 
        try: 
            user_result = float(user_answer) 
            if user_result == calculate(eq): 
                feedback = "أحسنت الإجابة صحيحة" 
                print(feedback) 
                text_to_speech(feedback) 
                correct_answers += 1  # Increment correct answer counter
            else: 
                correct_result = calculate(eq) 
                feedback = f"الإجابة خطأ والناتج الصحيح هو {correct_result}" 
                print(feedback) 
                text_to_speech(feedback) 
                incorrect_answers += 1  # Increment incorrect answer counter
        except ValueError: 
            feedback = "لم يتم التعرف على الإجابة" 
            print(feedback) 
            text_to_speech(feedback) 

# Print the counters
print(f"عدد الإجابات الصحيحة: {correct_answers}")
print(f"عدد الإجابات الخاطئة: {incorrect_answers}")
text_to_speech(f"عدد الإجابات الصحيحة: {correct_answers}")
text_to_speech(f"عدد الإجابات الخاطئة: {incorrect_answers}")

continue  # Restart the main loop after training 

# حساب الناتج 
result = calculate(expression) 
if result is not None: 
    print(f"الناتج هو: {result}") 
    # تحويل الناتج إلى صوت 
    text_to_speech(f"الناتج هو: {result}")


# In[2]:


# Define dummy functions for testing
def generate_similar_equations(expression):
    # Example implementation for testing
    return ["2 + 2", "3 + 3", "4 + 4"]

def calculate(expression):
    # Example implementation for testing
    return eval(expression)

def text_to_speech(text):
    # Example implementation for testing
    print(f"Speaking: {text}")

def get_audio():
    # Example implementation for testing
    # Return a string that can be converted to float for testing
    return "4"

# Initialize counters
correct_answers = 0
incorrect_answers = 0

# Define train_expression for testing
train_expression = "2 + 2"

# Generate and present similar equations 
similar_equations = generate_similar_equations(train_expression) 
for eq in similar_equations: 
    print(f"معادلة مشابهة: {eq}") 
    text_to_speech(f"معادلة مشابهة: {eq}") 
     
    # الحصول على إجابة المستخدم 
    user_answer = get_audio() 
    if user_answer: 
        try: 
            user_result = float(user_answer) 
            if user_result == calculate(eq): 
                feedback = "أحسنت الإجابة صحيحة" 
                print(feedback) 
                text_to_speech(feedback) 
                correct_answers += 1  # Increment correct answer counter
            else: 
                correct_result = calculate(eq) 
                feedback = f"الإجابة خطأ والناتج الصحيح هو {correct_result}" 
                print(feedback) 
                text_to_speech(feedback) 
                incorrect_answers += 1  # Increment incorrect answer counter
        except ValueError: 
            feedback = "لم يتم التعرف على الإجابة" 
            print(feedback) 
            text_to_speech(feedback) 

# Print the counters
print(f"عدد الإجابات الصحيحة: {correct_answers}")
print(f"عدد الإجابات الخاطئة: {incorrect_answers}")
text_to_speech(f"عدد الإجابات الصحيحة: {correct_answers}")
text_to_speech(f"عدد الإجابات الخاطئة: {incorrect_answers}")

# حساب الناتج 
expression = "2 + 2"  # Example expression for testing
result = calculate(expression) 
if result is not None: 
    print(f"الناتج هو: {result}") 
    # تحويل الناتج إلى صوت 
    text_to_speech(f"الناتج هو: {result}")


# In[3]:


import matplotlib.pyplot as plt

# بيانات العداد
correct_answers = 5  # مثال على عدد الإجابات الصحيحة
incorrect_answers = 3  # مثال على عدد الإجابات الخاطئة

# إنشاء قائمة بالبيانات
categories = ['RIGHT ANSWER', 'WORONG ANSWER']
values = [correct_answers, incorrect_answers]

# رسم بياني
plt.figure(figsize=(4, 5))
plt.bar(categories, values, color=['purple', 'yellow'])

# إضافة عناوين وتسمية المحاور
plt.title('NUMBER OF RIGTH AND WRONG ANSWER')
plt.xlabel('TYPE OF ANSWER')
plt.ylabel('NUMBER OF ANSWER')

# عرض القيم على الأشرطة
for index, value in enumerate(values):
    plt.text(index, value + 0.1, str(value), ha='center')

# عرض الرسم البياني
plt.show()


# In[ ]:




