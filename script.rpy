define frassati = Character("Frassati")

label start:

    play music "Gymnopédie No. 1 [TubeRipper.com].mp3"

    scene bg_first with fade
    "You find yourself in a quiet room, where a young man sits across from you with a gentle smile."

    show frassati at center with dissolve
    frassati "Ciao! I’m Pier Giorgio Frassati. I suppose you could say I’m a bit of a mountain climber, student, and sometimes troublemaker for good causes."

    "You smile, curious to learn more."

    frassati "I was born in 1901 in Turin, Italy, into a wealthy family. My father was a newspaper editor and even served as a senator."
    frassati "Despite all the privilege around me, I was always drawn to something... deeper. Something more than politics or success."

    scene bg_street with fade
    show frassati at center with dissolve
    frassati "Turin was a city of great contrast—fancy cafes and carriages on one street, and children begging on the next."
    frassati "Even as a kid, when I saw a poor man or someone sick, I couldn’t look away. I had to help."

    scene bg_room with fade
    show frassati at center with dissolve
    frassati "When I was a teen, I joined the Society of St. Vincent de Paul. It became a second home to me."
    frassati "I’d sneak out early or stay out late just to bring food, medicine, or warm clothes to the people living on the edges of society."
    frassati "People would ask me why I wasted so much time on the poor. But how could I not? That was Christ I was serving."

    scene bg_mountains with fade
    show frassati at center with dissolve
    frassati "I wasn’t always serious though. I loved to climb—literally! Hiking and skiing in the Alps was my passion."
    frassati "The mountains were where I felt closest to God. Each step upward was like prayer."
    frassati "Some people say holiness is boring. They never went hiking with me and my friends."
    frassati "We called ourselves 'The Tipi Loschi'—which means 'The Shady Characters.' It was our joke, because we were trying to be saints... but we didn’t want to take ourselves too seriously."

    scene bg_room with fade
    show frassati at center with dissolve
    frassati "I studied mining engineering. Not exactly glamorous, but I chose it because I wanted to help workers in the mines—those often forgotten."
    frassati "Faith wasn’t just about prayer—it had to mean something in the world. That’s why I got involved in politics too."
    frassati "I wasn’t loyal to any party. My loyalty was to truth, justice, and the dignity of the human person. Always."

    scene bg_hospital with fade
    show frassati at center with dissolve
    frassati "In 1925, everything changed. I got sick—polio, they said. Likely from someone I had helped in the slums."
    frassati "I didn’t tell anyone how bad it was. My grandmother had just died—I didn’t want to burden my family."
    frassati "Within a few days, I was paralyzed. Then bedridden. Then... gone."

    pause

    frassati "When I died, thousands of people showed up to my funeral. The streets were filled—not with politicians or famous people—but with the poor, the sick, the forgotten."
    frassati "They were my family, in a way. And I suppose they remembered me."
    frassati "I was 24 years old."

    scene bg_room with fade
    show frassati at center with dissolve
    frassati "Years later, I was beatified by Pope John Paul II. He called me 'the man of the Beatitudes.'"
    frassati "But if I’m remembered, I don’t want it to be because of fame or sainthood."
    frassati "I just want people to remember this: that it’s possible to live a full, joyful life for God—even in a short time."
    frassati "That every person you meet is Christ in disguise."
    frassati "And that real adventure begins when you stop living for yourself."

    jump ask_question

label ask_question:

    menu:
        "Tell me about your faith and how it shaped your life":
            jump faith_story
        "What was it like growing up in Turin and the mountains?":
            jump mountain_story
        "Why did you choose politics and engineering?":
            jump political_story
        "How did you spend your time helping the poor?":
            jump charity_story
        "That's all I wanted to ask.":
            jump goodbye

label faith_story:
    scene bg_room with fade
    show frassati at center with dissolve
    frassati "Faith wasn’t just something I practiced on Sundays. It was something I lived every day."
    frassati "I would go to Mass almost every day, sometimes early before my classes, sometimes sneaking away at lunch."
    frassati "It wasn’t easy, but it kept me grounded. I found that prayer was more powerful than I could ever imagine—especially when I was helping the poor."
    frassati "Faith is what gave my life meaning. It wasn’t about success, fame, or fortune—it was about service, love, and sacrifice."
    jump ask_question

label mountain_story:
    scene bg_mountains with fade
    show frassati at center with dissolve
    frassati "The mountains... oh, the mountains! I loved to climb them. They were my escape and my place to meet God."
    frassati "It was always a challenge, especially when we’d climb with our friends. But the views, the quiet, and the feeling of standing at the peak... that was something indescribable."
    frassati "And hiking with friends? It was the best. We’d pray together, laugh, and talk about life. That’s where I found peace."
    jump ask_question

label political_story:
    scene bg_room with fade
    show frassati at center with dissolve
    frassati "Politics was a way to fight for justice. But it wasn’t about being part of a party—it was about the truth and dignity of the human person."
    frassati "I got involved because I couldn’t sit idly by while injustice was happening. I worked with others to resist the rise of fascism, even when it was dangerous."
    frassati "Being politically active wasn’t about popularity for me. It was about doing the right thing, no matter what the cost."
    jump ask_question

label charity_story:
    scene bg_street with fade
    show frassati at center with dissolve
    frassati "Helping the poor was my calling. I didn’t do it for recognition, but because it was what Jesus asked of us."
    frassati "Whether it was bringing food to the sick or helping with daily needs, I saw Christ in each person I met."
    frassati "I didn’t want others to suffer in silence, and so I always tried to show love, even in the smallest ways."
    jump ask_question

label goodbye:
    scene bg_room with fade
    show frassati at center with dissolve
    frassati "It was a pleasure talking with you. Remember: live for something greater!"
    return
