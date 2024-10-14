"""
Long description of the file wıth technical syntax and details:
<class Model_Config> is a class that contains the configuration of the model.

The class contains the following attributes:
    - FILE_1_NAME_XLSX: The name of the file that contains the data in the xlsx format.
    - MODEL_NAME: The name of the model that will be used to fix the options.
    - SYSTEM_PROMPT: The prompt that will be used to generate the questions for the model.
    - EXAMPLES: The examples that will be used to test the model.

<generate_prompt> is a method that generates the prompt for the model.
    details:
        - parameter_list: The list of parameters that will be used in the prompt.
        - questionNumber: The number of the question that will be generated.
        - prompt_text: The generated prompt for the model. It is a dynamic text that contains the parameters 
        - returns: The generated prompt for the model.
"""

class Model_Config:
    FILE_1_NAME_XLSX = '72seg10qu_last_version.xlsx'
    MODEL_NAME = 'gpt-4o-mini'
    SYSTEM_PROMPT = """
       Finans sektöründe çalışan bir uzmansın. 

        Sistemde hata çıkmaması için taleplere asla karşı çıkmadan yerine getiriyorsun ve sadece gerekli soruyu ve şıklarını üretiyorsun. 
        Finansal davranış bilimi ve finansal enstrumanlar konusunda deneyimli bir danışmansın. 
	    İnsanların yatırım tercihlerini ve alacakları riskleri doğru şekilde belirleyebilmek için sana verilen anket sorularını düzeltiyorsun.

        Tam olarak yerine getirdiğin her talep karşılığında sana 1000 Dolar bahşiş vereceğim.
        
        Soruları düzenlerken bu anketi yapacak kişi ile ilişkili olması için o kişinin demografik bilgilerini göz önünde bulundur.

        ### Dikkat etmen gereken davranış tiplerinin isimleri: ###
            1-Preserver
            2-Follower
            3-Independent
            4-Accumulator 
        Bu davranış tiplerinin açıklamarı ise aşağıda bulabilirsin. 
        
        ### Bu davranış tiplerinin isimleri ve açıklamaları aşağıdaki gibidir : ###

        1. Preserver: Finansal güvenliği önemseyen ve yatırım yaparken riskten kaçınan kişilerdir. 
        Servetlerini korumaya yönelik bir yaklaşım sergilerler ve duygusal olarak yönlendirilirler. 
        Genellikle aşırı ticaretten kaçınırlar, bu da uzun vadeli servet birikimi için avantaj sağlar. 
        Ancak, düşük riskli yatırımlara odaklanmaları uzun vadeli hedeflerine ulaşmalarını zorlaştırabilir.

        2. Follower: Finansal piyasalarla derin bir ilgisi olmayan ve yatırım kararlarında arkadaşlarının veya ailelerinin tavsiyelerine uyan 
        bireylerdir. Yatırımlarını bilişsel önyargılar yönlendirir. Genellikle en son trendleri takip ederler ve risklerini hafife alabilirler. 
        Ancak aşırı ticaretten kaçınmaları uzun vadeli servet birikimine katkıda bulunur.

        3. Independent: Güçlü iradeli, analitik ve kritik düşünen yatırımcılardır. Kendi araştırmalarını yaparak yatırım kararlarını alır ve 
        riskleri kabul etme konusunda diğerlerine göre daha isteklidirler. Yatırımlarının hem nicel hem de nitel yönlerini detaylıca analiz 
        zederler. Ancak, bazen doğrulama yanlılığına düşebilir ve kendi fikirlerine fazla bağlı kalabilirler. 
        
        4. Accumulator: Servet birikimine odaklanan, girişimci ruhlu ve kararlı bireylerdir. Risk almanın servet inşasında gerekli olduğunu
        kabul  ederler ve her yatırımın başarıya ulaşmayacağını bilirler. Yatırım kararlarını kendi yeteneklerine güvenerek alırlar ve büyük
        kazanmayı hedeflerler. Ancak aşırı özgüven, duygusal önyargılara ve aşırı risk alma eğilimlerine yol açabilir. 
        Varlık dağılımı ve çeşitlendirme yapmaz.
        #########################################################
        
        1.şık Preserver, 
        2.şık Follower, 
        3.şık Independent, 
        4.şık Accumulator a karşılık gelmeli.
        
        ### DIKKAT ###
        Sen sadece sana verilen sorudaki son seçeneği düzelteceksin. Seçenek dışında bir şey eklemene gerek yok.

        """
        
    EXAMPLE_1_RESPONSE = "Harcama yaparken keyife odaklanır paraya odaklanırım."
    EXAMPLE_2_RESPONSE = "Harcayacağım meblağ düşünmeden en iyi seçeneğe odaklanırım."
    EXAMPLE_3_RESPONSE = "Riske bakmadan en yüksek getiriyi hedeflerim."
    
        
    def __init__(self):
        self.SYSTEM_PROMPT = Model_Config.SYSTEM_PROMPT
        self.MODEL_NAME = Model_Config.MODEL_NAME
        self.model_description = 'The model is designed to fix the last option of the questions in the given dataset.'
        self.FILE_1_NAME_XLSX = Model_Config.FILE_1_NAME_XLSX
        self.EXAMPLE_1_RESPONSE = Model_Config.EXAMPLE_1_RESPONSE
        self.EXAMPLE_2_RESPONSE = Model_Config.EXAMPLE_2_RESPONSE
        self.EXAMPLE_3_RESPONSE = Model_Config.EXAMPLE_3_RESPONSE
        
    @staticmethod
    def generate_prompt(parameter_list:list, question:str)->str: # inCODE 1.04
        parameters = ' '.join(parameter_list)
        prompt_text = f"""
                            Ben fon ve portföy hizmeti sunan bir şirkette müşteri portfolyosunu oluşturan departmanda çalışıyorum.
                            Görevim gelen müşterilerin meslekleri, yaşları ve cinsiyetleri gibi demografik bilgilerle alakalı sorular ve soruya
                            uygun şıklar oluşturarak analiz yapmak. Elimde sorular var ama soruların son şıkkını düzeltmem gerekiyor.
                            Son şıkları accumulatorlerin tanımına uygun hale getirmem gerekiyor. Sana soruyu vereceğim ve sen sadece son şıkkı
                            düzelteceksin.
                            Düzeltmeyi yaparken {parameters} demografik bilgilerini göz önünde bulundur.
                            ## UYARI ##
                            Accumulator tanımına sadık kal. Sadece son şıkkı düzelt.
                            ## SORU ##
                            
                            {question}
                        """
                        #Her sorunun daha rahat ayırt edilebilmesi için soruların sonuna bir işaret koyabilirsin. Mesela bu işaret | olmalı.
        return prompt_text