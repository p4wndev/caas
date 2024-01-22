# rasa run --model D:\CAAS\api-rasa-cntt\models\nlu-20231220-152751.tar.gz --endpoints D:\CAAS\api-rasa-cntt\endpoints.yml --credentials D:\CAAS\api-rasa-cntt\credentials.yml
# rasa train --domain D:\CAAS\api-rasa\api-cntt\domain.yml --config D:\CAAS\api-rasa\config\config-cntt.yml --data D:\CAAS\api-rasa\api-cntt\data\nlu.yml D:\CAAS\api-rasa\api-cntt\data\stories.yml

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from api_gemini.api_gemini import gpt


from api_voiceflow import api_data

class ActionGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Hãy trả lời câu "+ str(textex) +", đồng thời hỏi tên người đó và không nói tiếp bất cứ gì hết."
        answer=gpt(text)
        dispatcher.utter_message(response="utter_greet",text =  answer)
        return []
    
class ActionGoodbye(Action):
    def name(self):
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định tạm biệt (goodbye). Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)
        dispatcher.utter_message(response="utter_goodbye",text =  answer)
        return []
    
class ActionThank(Action):
    def name(self):
        return "action_thank"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định cảm ơn người dùng. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)
        dispatcher.utter_message(response="utter_thank",text =  answer)
        return [] 

class ActionHelp(Action):
    def name(self):
        return "action_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với chức năng hỗ trợ người dùng định hướng nghề nghiệp và trả lời các câu liên quan tới tuyển sinh. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)
        dispatcher.utter_message(response="utter_help",text =  answer)
        return [] 
    
class ActionAskName(Action):
    def name(self):
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Nếu là câu chào thì chào lại và đặt câu hỏi hỏi tên người dùng, ngược lại thì trả lời ngắn gọn không đặt câu hỏi. Trả lời câu" + textex + " một cách ngắn gọn"
        answer=gpt(text)

        dispatcher.utter_message(response="utter_ask_name",text =  answer)
        return [] 
    
class ActionProfile(Action):
    def name(self):
        return "action_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định cho đường link nộp hồ sơ cho trường đại học. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)
  
        
        dispatcher.utter_message(response="utter_profile",text =  answer)
        return [] 
class ActionDormitory(Action):
    def name(self):
        return "action_dormitory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định giới thiệu kiến túc xá. Hãy trả lời câu " + textex + " một cách ngắn gọn với dữ kiện " + api_data(textex)
        answer=gpt(text)
        # name = tracker.get_slot("name")
        # majors =tracker.get_slot("majors")
        # university =tracker.get_slot("university")
        # intent = tracker.latest_message.get('intent', {})
        
        dispatcher.utter_message(response="utter_dormitory",text =  answer)
        return []
    
class ActionFacilities(Action):
    def name(self):
        return "action_facilities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định giới thiệu cơ sở vật chất. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_facilities",text =  answer)
        return [] 
    

class ActionTime(Action):
    def name(self):
        return "action_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định giới thiệu kiến túc xá. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_time",text =  answer)
        return []
    
class ActionBenchmark(Action):
    def name(self):
        return "action_benchmark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        major=tracker.get_slot("majors")
        university=tracker.get_slot("university")
        text = f"Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Cho biết điểm chuẩn là {api_data(textex)} . Hãy trả lời câu " + textex +" một cách văn vẻ hơn trong 2 dòng"
        answer=gpt(text)


        dispatcher.utter_message(response="utter_benchmark",text =  answer)
        return [] 
    
    
    
class ActionTuition(Action):
    def name(self):
        return "action_tuition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với học phí đại trà là 17 triệu. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_tuition",text =  answer)
        return [] 
    
    
class ActionCurriculum(Action):
    def name(self):
        return "action_curriculum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Hãy trả lời câu " + textex + " một cách ngắn gọn với gợi ý là " + api_data(textex)
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_curriculum",text =  answer)
        return [] 

class ActionCriterias(Action):
    def name(self):
        return "action_criterias"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với chỉ tiêu chung là "+ api_data(textex) +". Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_criterias",text =  answer)
        return [] 

class ActionReview(Action):
    def name(self):
        return "action_review"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định giới thiệu về trường. Hãy trả lời câu " + textex + " một cách ngắn gọn với gợi ý là: " + api_data(textex)
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_review",text =  answer)
        return [] 



    
 

class ActionCareerOpportunities(Action):
    def name(self):
        return "action_career_opportunities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Ý định là về cơ hội nghề nghiệp và học tập. Hãy trả lời câu " + textex + " một cách ngắn gọn với gợi ý là " + api_data(textex)
        answer=gpt(text)


        
        dispatcher.utter_message(response="utter_career_opportunities",text =  answer)
        return [] 

class ActionTeach(Action):
    def name(self):
        return "action_teach"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Với dự định kiến thức môn học. Hãy trả lời câu " + textex + " một cách ngắn gọn với gợi ý là: " + api_data(textex)
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_teach",text =  answer)
        return []

class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục tên là: 'CAAS'. Hãy trả lời câu " + textex + " một cách ngắn gọn mang tính giáo dục, những câu hỏi khác không nên trả lời"
        answer=gpt(text)

        
        dispatcher.utter_message(response="utter_default_fallback",text =  answer)
        return [] 
