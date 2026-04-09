import speech_recognition as sr 
import webbrowser
r = sr.Recognizer()

songDict = {
    "street by street":"https://open.spotify.com/track/42Ly3cfDuDaLZGvgOTwvLi?si=5ee1ee7757d14caf",
    "magnolia":"https://open.spotify.com/track/0R5vO904RzxDJ30yZaspQD?si=a980f0ef489e4623",
    "like the movies":"https://open.spotify.com/track/1hUXDEqjNIIbfjTcaz3jzb?si=31d86ce5c07d43ed",
    "i wish you love":"https://open.spotify.com/track/5zHLswJplBXyPstFSSMIOH?si=020fcb3cecd64081",
    "james":"https://open.spotify.com/track/2y1NtQ2ZfIq0zBUP3tOlbX?si=05becd6bd8e74296",
    "someone new":"https://open.spotify.com/track/3EZM5cS4hxty3MAcuBNj1H?si=3160208198744f69",
    "best friend":"https://open.spotify.com/track/5zQR0qoA4S1Iwj2bAwW03a?si=69efccdd207a4a48",
    "let you break my heart again":"https://open.spotify.com/track/709p9UGPAuyImWf1Z3vjRo?si=a9d91769e89f445e",
    "love flew away":"https://open.spotify.com/track/5Uro6tis4oexrT4Po1q71H?si=59dd419caa39416b",
    "a night to remember":"https://open.spotify.com/track/180AbZduI6bYQIzwCHRwu9?si=c2dda01407264796",
    "santa baby":"https://open.spotify.com/track/4jHl6jgzZOnS4nGamPZ1Uk?si=28d8e1794a4a421c",
    "winter wonderland":"https://open.spotify.com/track/7CeP2uqPli3AW6Fn6OF70L?si=1135c397bf194bad",
    "christmas dreaming":"https://open.spotify.com/track/4TPrijO5HV5f6ovpf2E10i?si=b75740ec9572494d",
    "the christmas waltz":"https://open.spotify.com/track/7HCMTcTZM6i2SKZjBtWqkc?si=f93284e4e9634f8d",
    "santa claus is coming to town":"https://open.spotify.com/track/5h1LioQgmLvWoRU7V4pjma?si=e77732b6742e4e2c",
    "christmas magic":"https://open.spotify.com/track/6Dpex5v3xDRTaIW8dcdvP2?si=451abc9788c2472c",
    "love to keep me warm":"https://open.spotify.com/track/0Ue7cb3mm8wxbvkpJVVE4I?si=4a1e137f183f4aa5",
    "fragile":"https://open.spotify.com/track/0TveByn1xvhUjVrvjsWrTf?si=40fec47bbab84da1",
    "beautiful stranger": "https://open.spotify.com/track/2EDxQGcJlVi32jBCXzUZhL?si=a6cc8d9665354a87",
    "valentine":"https://open.spotify.com/track/5cxeDbK7ZEefo866N1vE8m?si=5d30801f72a7486d",
    "above the chinese restaurant":"https://open.spotify.com/track/04cnoAgTzNnV1skGbWJeTM?si=8a9498810ea54346",
    "dear soulmate":"https://open.spotify.com/track/1yDvme1TNme1B9qWArp6c1?si=90377ad7eff945ba",
    "what love will do to you":"https://open.spotify.com/track/37nBLmvdfeqq8HrsMp2RmR?si=5acd37a1d9da428e",
    "i've never been in love before":"https://open.spotify.com/track/4UDus24wWxzVM1uCbkRFNF?si=6143261f12bc4c72",
    "just like chet":"https://open.spotify.com/track/3s31XYGfswV1CR3UFCP2Sx?si=4224ebe2ba2b4359",
    "everything i know about love":"https://open.spotify.com/track/5Df8LivqhhpY5m8eT8st70?si=9c358724a0804642",
    "falling behind":"https://open.spotify.com/track/0mlIVjrhLn8WvmK1F9cgzY?si=e6ffca4d877a47ab",
    "hi":"https://open.spotify.com/track/6cBbx14y271qwBX2CQttwQ?si=6b662e5c16c947ca",
    "dance with you tonight":"https://open.spotify.com/track/6PAfPRBtkg2YR72cHtc7oK?si=d19c75d0bbae4130",
    "night light":"https://open.spotify.com/track/6dJyKQaxxsxQA0rPF8JmNg?si=129d30bffb174493",
    "slow down":"https://open.spotify.com/track/4KLZOU5V5XuEkvytSgyW6u?si=b4976375b81f4d66",
    "lucky for me":"https://open.spotify.com/track/4pOTM8mcaosHV1SbcJg4xl?si=c0741dd4907f41b7",
    "questions for the universe":"https://open.spotify.com/track/7kle3wveNJelYdI1khvHDb?si=736fbf07aa5a4873",
    "dreamer":"https://open.spotify.com/track/59ufJBDa8L0dduJwcxXnZj?si=51e48c18e2bb4446",
    "second best":"https://open.spotify.com/track/7sOUsRHqnu18iSYE0KM11f?si=2042faa122cc4893",
    "haunted":"https://open.spotify.com/track/6HD9dZsgPNrfu3cF1hqDob?si=a31544c3c3994d47",
    "must be love":"https://open.spotify.com/track/2JGbFWHHaEI06ju458U1bI?si=e695cc3a3a3b4aea",
    "while you were sleeping":"https://open.spotify.com/track/2vYe5IUwGeU3JgEZhxhKey?si=b2b09f73867c4fff",
    "lovesick":"https://open.spotify.com/track/4bKuWOD35m2axLUKh5h3sl?si=9cc63da226814cc5",
    "california and me":"https://open.spotify.com/track/7LviscbwsdfnVv1VYwx7l0?si=805a70b3a8d64761",
    "nocturne":"https://open.spotify.com/track/7d10kpDvGHt2F2vIBewbFr?si=41ae2621b4e84b8b",
    "promise":"https://open.spotify.com/track/4kfAR8qSzipaG0K9Uw7qp6?si=eaaf0a0763584720",
    "from the start":"https://open.spotify.com/track/29Gys08x2u3ZSERTe0WvbE?si=1f8f8155f496491e",
    "misty":"https://open.spotify.com/track/07glT1JH8qWRe3Om4dGcrC?si=a50699ff82e44122",
    "serendipity":"https://open.spotify.com/track/0IcQVGl2Y8Rkf6ezmn4RHD?si=efdad02cef2641d4",
    "letter to my 13 year old self":"https://open.spotify.com/track/2zlvJLzZdU00biRqmxQBNA?si=791a3ae2becf464b",
    "bewitched":"https://open.spotify.com/track/2e0txm9dWOYCWbfUvPqU75?si=f9164aaeea6d48c6",
    "bored":"https://open.spotify.com/track/2SPbioo65CuUB3H0aW1ID5?si=587bdbe9cead4434",
    "trouble":"https://open.spotify.com/track/0Ah2wJirVEGUITkcPU6ali?si=e51423c18a834b69",
    "it could happen to you":"https://open.spotify.com/track/1pyfaPU3aw8JorXRJQf6cs?si=e193514451604e73",
    "goddess":"https://open.spotify.com/track/2SEeyc2KS9DIjiJPCYtfgJ?si=0016bdd01cba41b1",
    "clockwork":"https://open.spotify.com/track/1zOXs9kBDCGVYZXbxCR3eu?si=71014e4c87c648dc",
    "lover girl":"https://open.spotify.com/track/4nwjvcUjV7cexhwA40Bh5i?si=ceb5b8ad8f38410f",
    "snow white":"https://open.spotify.com/track/1AZwVoUx3UF5JbkUeMSUGe?si=ce5a4dc9c4fb48f6",
    "castle in hollywood":"https://open.spotify.com/track/3zTnSPti5JjNsowJH4SS3u?si=a0846ccb49f1493c",
    "carousel":"https://open.spotify.com/track/1f1v2sHXpFFtjxB8KVKypW?si=9c9bbec30afe417a",
    "silver lining":"https://open.spotify.com/track/4kfXaAAZlfBrimPJYHlCEM?si=1ba3c4c45590400a",
    "too little, too late":"https://open.spotify.com/track/6zEg4KEgz6RGhCPmDKplYf?si=e8bf965cf4d943e6",
    "cuckoo ballet":"https://open.spotify.com/track/6iGT4CugvKIPPee1BfNRTp?si=81fb2da0b9c64204",
    "forget me not":"https://open.spotify.com/track/3cm2v6gfWuixcHL2A6wvGl?si=d14a08dab7bb44b1",
    "tough luck":"https://open.spotify.com/track/5PFjKfGf75I3LkKGiReWp5?si=afc23959af1a48e2",
    "a cautionary tale":"https://open.spotify.com/track/00k7tsWaAJXGJ4rZZxd6bM?si=3d3f052d5af3429d",
    "mr. eclectic":"https://open.spotify.com/track/0gBlPhTZaqY06DHCL9V7W5?si=c0c5e7a609764e2b",
    "clean air":"https://open.spotify.com/track/5vUwvYW5fpHrwHfirVpkHn?si=0955ab187b8e4611",
    "sabotage":"https://open.spotify.com/track/1fUp9sWmy3EiZzPGbJmR4W?si=8c877372f93a405f",
    "seems like old times":"https://open.spotify.com/track/5mAFfXu5wUJWicmzxjJRKo?si=f826e43108864867",
    "how i get":"https://open.spotify.com/track/1gjrb6iiP6KIrQnDBIqqDi?si=3ff27054ab384e71"
}

songList = list(songDict)
currentlyListening = True

while currentlyListening:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=3)
        audio_text = r.listen(source)
        #r.recognize_google(audio_text) gives you the audio as text
        try:
            text = r.recognize_google(audio_text)
            for song in songList:
                if song in text:
                    webbrowser.open_new(songDict[song])
            if "stop listening" in text:
                currentlyListening = False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
