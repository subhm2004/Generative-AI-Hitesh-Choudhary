# Strings and its methods (strings are immutable)

chai_type = "Masala chai"
customer_name = "Shubham"

print(f"Order for {customer_name} : {chai_type} please !")

# string slicing 
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}") # str[0...7]
print(f"First word: {chai_description[:8:2]}") # str[0...7] skipping 2 char 

print(f"Last word: {chai_description[12:]}")# str[12....end_of_str]

print(f"Last word: {chai_description[::-1]}") # reverse kr dega string ko 

# encoded string

#encoding
label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8") #commin way of encoding

print(f"Non Encoded label: {label_text}")
print("\n")

print(f"Encoded label: {ecoded_label}")
print("\n")

# decoding
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")