# Data processing concepts


class Solution():
    
    def match_animation_to_song(self, songs: list[str], animations: list[str]) -> list[str]:
        
        res = []
        
        for song in songs:
            
            s = song.split(":")
            for i in range(len(animations)):
                
                a = animations[i].split(":")
                
                if int(a[1]) > int(s[1]):
                    continue
                
                time_played = int(s[1]) / int(a[1])
                
                if time_played.is_integer():
                    
                    name = a[0]
                    time = str(int(time_played))
                    res.append(name + ":" + time)
                    break
        
        return res
        

songs = ["notion:180", "voyage:185", "sample:180"]
animations = ["circles:360", "squares:180", "lines:37"]

sol = Solution()

res = sol.match_animation_to_song(songs, animations)

print(res)
