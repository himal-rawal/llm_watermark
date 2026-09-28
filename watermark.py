class Watermark:
    replacebale_char_glymphs={
    "a": "а",
    "o": "о",
    "x": "х",
    "w": "ԝ"
}
    zw_char="\u200b"
    zw_char_nonjoiner="\u200c"
    signature="Himal"
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
        signature_bytes = self.signature.encode('utf-8')
        signtature_bits= self.bytes_to_bits(signature_bytes)
        watermark=self._encode_bits(signtature_bits)
        return watermark + text + watermark

    def bytes_to_bits(self,bytes):
        result=[]
        for byte in bytes:
            result.append(format(byte,'08b'))
        return "".join(result)

    def _encode_bits(self,bits):
        parts=[]
        for bit in bits:
            if bit == "1":
                parts.append(self.zw_char)
            else:
                parts.append(self.zw_char_nonjoiner)
        return "".join(parts)

# Adding watermark
    def add_watermark(self, text):
        homoglyph_text = self._add_homoglyph_watermark(text)
        zerowidth_text = self._add_zerowidth_watermark(homoglyph_text)
        return zerowidth_text

    def detect_watermark(self, text):
        hasWatermark=self.detect_zerowidth_watermark(text) or self.detect_homoglyph_watermark(text)
        return hasWatermark
    
    def detect_homoglyph_watermark(self,text):
        glyph_words=set(self.replacebale_char_glymphs.values())
        for char in text:
            if char in glyph_words:
                return True
        return False

    def detect_zerowidth_watermark(self,text):
        if not text:
            return False
        signature_bits = self.bytes_to_bits(self.signature.encode("utf-8"))
        expected_marker = self._encode_bits(signature_bits)
        return text.startswith(expected_marker) and text.endswith(expected_marker)