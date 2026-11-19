# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 387 (printed ٣٨٦)."""

PAGE_NUMBER = 387
PRINTED_PAGE = "٣٨٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وصفة) نحو: «اضربه» at the foot of PDF p. 386.
    {"type": "matn",
     "ar": "ضربا ما» أي: ضربا أي ضرب كان.",
     "en": "…ḍarban mā” (strike him with some sort of striking), that is, a striking of whatever kind it may be."},
    {"type": "matn",
     "ar": "(و«من» كذلك) أي: يكون موصولة نحو: «أكرمت من جاءك»، واستفهامية نحو: «من غلامك؟ ومن ضربت؟»، وشرطية نحو: «من تضرب أضرب»،",
     "en": "(And “man” is likewise), that is, it is relative, as in “akramtu man jāʾaka” (I honoured whoever came to you); interrogative, as in “man ghulāmuka?” (who is your servant?) and “man ḍarabta?” (whom did you strike?); conditional, as in “man taḍrib aḍrib” (whomever you strike, I shall strike);"},
    {"type": "matn",
     "ar": "وموصوفة إما بمفرد نحو قوله:",
     "en": "and qualified, either by a single word, as in the poet’s words:"},
    {"type": "verse",
     "ar": "وكفى بنا فضلا على من غيرنا     حب النبي محمد إيانا",
     "en": "It suffices us as a merit over someone other than us / that the Prophet Muḥammad loves us,"},
    {"type": "matn",
     "ar": "أي: شخص غيرنا.",
     "en": "that is, “a person other than us”;"},
    {"type": "matn",
     "ar": "أو بجملة نحو: «من جاءك قد أكرمته» (إلا في التامة والصفة) فإن كلمة «من» لا تجيء تامة ولا صفة.",
     "en": "or by a sentence, as in “man jāʾaka qad akramtuhu” (someone who came to you I have honoured); (except in the complete and the qualifier [uses]), for the word “man” does not occur as complete nor as a qualifier."},
    {"type": "matn",
     "ar": "(و«أي») للمذكر (و«أية») للمؤنث (كـ«من») في ثبوت الأمور الأربعة، وانتفاء التامة والصفة،",
     "en": "(And “ayy”) for the masculine (and “ayya”) for the feminine (are like “man”) in having the four [uses] and lacking the complete and the qualifier [uses]."},
    {"type": "matn",
     "ar": "فـ«أي» الموصولة نحو: «اضرب أيهم لقيت»، والاستفهامية نحو: «أيهم أخوك؟ وأيهم لقيت؟»،",
     "en": "So relative “ayy” is as in “iḍrib ayyahum laqīta” (strike whichever of them you met); the interrogative, as in “ayyuhum akhūka?” (which of them is your brother?) and “ayyahum laqīta?” (which of them did you meet?);"},
    {"type": "matn",
     "ar": "والشرطية نحو قوله تعالى: ﴿أيا ما تدعوا فله الأسماء الحسنى﴾[[١]]، والموصوفة نحو: «يا أيها الرجل»[[٢]].",
     "en": "the conditional, as in His words, the Exalted: “Whichever you call upon, to Him belong the most beautiful names”; and the qualified, as in “yā ayyuhā al-rajulu” (O you, the man)."},
    {"type": "matn",
     "ar": "قيل: «أي» يقع صفة اتفاقا، فلم جعلها المصنف كـ«من» التي لا تقع صفة أصلا؟",
     "en": "It has been said: “ayy” occurs as a qualifier by agreement, so why did the author make it like “man”, which never occurs as a qualifier at all?"},
    {"type": "matn",
     "ar": "وأجيب: بأن «أيا» الواقعة صفة هي في الأصل استفهامية؛ لأن معنى «مررت برجل أي رجل» أي: رجل عظيم يسأل عن حاله لا يعرفه كل أحد، فنقلت عن الاستفهامية إلى الصفة.",
     "en": "The answer given is that the “ayy” that occurs as a qualifier is in origin interrogative, because the meaning of “marartu bi-rajulin ayyi rajulin” (I passed by a man—what a man!) is “a great man whose condition is asked about, whom not everyone knows”; so it was transferred from the interrogative to the qualifier."},
    {"type": "matn",
     "ar": "(وهي) أي: كل واحدة من «أي» و«أية» (معربة) بالاتفاق (وحدها[[٣]]) لا يشاركها في الإعراب غيرها من الموصولات، إلا على اختلاف في «اللذان واللتان» وفي «ذو الطائية»،",
     "en": "(And it), that is, each of “ayy” and “ayya”, (is declinable) (muʿraba) by agreement, (alone): no other relative noun shares inflection with it, except with disagreement over “alladhāni” and “allatāni” and over the Ṭayyiʾ “dhū”."},
    {"type": "matn",
     "ar": "وإنما أعربت؛ لأنه التزم فيها الإضافة إلى المفرد التي هي من خواص الاسم المتمكن، فلا يرد «حيث وإذ وإذا»",
     "en": "It is declinable only because annexation to a single word, which is a property of the fully declinable noun (al-ism al-mutamakkin), is required with it; so “ḥaythu”, “idh” and “idhā” are no objection."},
    {"type": "matn",
     "ar": "(إلا إذا) كانت موصولة (حذف صدر صلتها[[٤]])",
     "en": "(Except when), being relative, (the first part of its relative clause has been elided)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الإسراء: ١١٠.",
     "en": "Qurʾān, Sūrat al-Isrāʾ 17:110."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا أعرف كونها معرفة موصوفة إلا في النداء. وأجاز الأخفش كونها نكرة موصوفة.",
     "en": "Shaykh al-Raḍī said: I do not know of its being a qualified definite noun except in the vocative. Al-Akhfash allowed its being a qualified indefinite noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "نص بقوله: وحدها على رد إعراب اللذان وذو الطائية.",
     "en": "By his word “alone” he stated explicitly the rejection of the declinability of “alladhāni” and of the Ṭayyiʾ “dhū”."},
    {"type": "pair",
     "ar": "وقد ضيع الشارح ما قصده بجعل بيانه مختصا بما هو المتفق، فافهم.",
     "en": "The commentator lost what he intended by making his explanation restricted to what is agreed upon; so understand."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وكانت مضافة، ويكون الصدر عائدا، فيبنى على الضم، وسيبويه يجيز إعرابها أيضا، فإن لم يكن مضافة، فأعربت.",
     "en": "And it is annexed, and the [elided] first part is the referring pronoun; then it is indeclinable with ḍamma. Sībawayh also allows its being inflected. If it is not annexed, it is inflected."},
]
