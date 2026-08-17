class Watermark:

    replacebale_char_glymphs={
    "a": "а",
    "o": "о",
    "x": "х",
    "w": "ԝ"
}
# Watermark by Homoglyph
    def _add_homoglyph_watermark(self,text):
        result=[]
        for char in text:
            
            if char in self.replacebale_char_glymphs:
                result.append(self.replacebale_char_glymphs[char])
            else:
                result.append(char)
        return "".join(result)
# Watermark by zerowidth
    def _add_zerowidth_watermark(text):
        return
#  
    def add_watermark(self, text):
        return 


    def detect_homoglyph_watermark(self,text):
        glyph_words=set(self.replacebale_char_glymphs.values())
        for char in text:
            if char in glyph_words:
                return True
        return False
