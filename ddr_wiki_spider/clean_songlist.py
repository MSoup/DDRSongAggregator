#Takes the data and cleans it
import json

text = r"ddr_wiki_spider/ddr_songlist.json"

with open(text, "r") as read_file:
  with open (r"output", "a+") as write_file:
    song_list = json.load(read_file)
    for song in song_list[0:10]:
      write_file.writelines(f"{song['song']} \n")



