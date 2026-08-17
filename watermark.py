class Watermark:

    replacebale_char_glymphs={
    "a": "а",
    "o": "о",
    "x": "х",
    "w": "ԝ"
}
    zw_char="\u200b"
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
    def _add_zerowidth_watermark(self,text):
        # For now we will append zero width character at the beginning and at the end
        # of the text but later we will add our own signatiure inside those text.
        # We will encode our secret text in zero width character and insert it inside
        # real text .ie if Himal  is the signature we will encode it with utf8  to 
        # values 72,105 basically we will convert unicode characters to bytes then we convert
        # those bytes to 8 bit binary digit and map with zero width space and zero width
        # non joiners. we can assign zero width space to 1 and another to 0  and then  
        # insert  the output signature to original text
         
       
        return self.zw_char + text + self.zw_char
#  
    def add_watermark(self, text):
        homoglyph_text = self._add_homoglyph_watermark(text)
        zerowidth_text = self._add_zerowidth_watermark(homoglyph_text)
        return zerowidth_text

    
    def detect_homoglyph_watermark(self,text):
        glyph_words=set(self.replacebale_char_glymphs.values())
        for char in text:
            if char in glyph_words:
                return True
        return False

    def detect_zerowidth_watermark(self,text):
       hasWatermark=text.startswith(self.zw_char) and text.endswith(self.zw_char)
       return hasWatermark