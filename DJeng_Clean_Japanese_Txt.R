library(RcppMeCab)
#Import File
jp_text <- read.csv("~/Documents/Statistical Software/jp_text.txt")

jp_text$text <- as.character(jp_text$text)

#Filter out symbols and unwanted text
jp_text$text <- str_replace_all(jp_text$text,"【","")
jp_text$text <- str_replace_all(jp_text$text,"】","")
jp_text$text <- str_replace_all(jp_text$text,"https//tco/[A-z,0-9]* ","")
jp_text$text <- str_replace_all(jp_text$text,"！","")
jp_text$text <- str_replace_all(jp_text$text,"『"," ")
jp_text$text <- str_replace_all(jp_text$text,"』"," ")
jp_text$text <- str_replace_all(jp_text$text,"「","")
jp_text$text <- str_replace_all(jp_text$text,"」"," ")
#This line specifically filters out emojis
jp_text$text <- str_replace_all(jp_text$text,"\\p{So}|\\p{Cn}","")
jp_text$text <- str_replace_all(jp_text$text,"RT ","")
jp_text$text <- str_replace_all(jp_text$text,"#","")
jp_text$text <- str_replace_all(jp_text$text,"@","")
jp_text$text <- str_replace_all(jp_text$text,"・"," ")
jp_text$text <- str_replace_all(jp_text$text,"、"," ")
jp_text$text <- str_replace_all(jp_text$text,"…","")
jp_text$text <- str_replace_all(jp_text$text,"https//tco/[A-z,0-9]*","")
jp_text$text <- str_replace_all(jp_text$text," ","")

#Data frame with word and character count
word_count <- data.frame(word=as.character("test"),number=1)

#Running this can take very long but it works
for (i in 1:nrow(jp_text)) {
  current_sentence <- pos(jp_text$text[i],format="data.frame")$token
  for (j in 1:length(current_sentence)) {
    current_word <- as.character(current_sentence[j])
    for (k in 1:nrow(word_count)) {
      if (current_word == as.character(word_count$word[k])) {
        word_count$number[k] <- word_count$number[k] + 1
        break
      } else if (k == nrow(word_count)) {
        new_word <- data.frame(word=current_word,number=1)
        word_count <- rbind(word_count,new_word)
      }
    }
  }
}



