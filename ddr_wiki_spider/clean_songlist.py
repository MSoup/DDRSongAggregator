#Takes the data and cleans it
import json

text = r"ddr_wiki_spider/songlist_detailed.json"

with open(text, "r") as read_file:
  with open (r"output.txt", "a+") as write_file:
    song_list = json.load(read_file)
    for song in song_list[0:20]:
      write_file.writelines(f"{song['song']} \n")




