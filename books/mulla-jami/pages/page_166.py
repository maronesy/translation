# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 166 (printed ١٦٥)."""

PAGE_NUMBER = 166
PRINTED_PAGE = "١٦٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "يصحح وقوعه مبتدأ (مثل: «في الدار رجل») فإن «في الدار» خبر يخصص المبتدأ بتقديمه كما عرفت، فلو أخر لبقي المبتدأ نكرة غير مخصصة.",
     "en": "…validates its occurring as a mubtadaʾ—“as in: ‘In the house is a man’ (fī al-dāri rajulun)”; for “in the house” is a khabar that specifies the mubtadaʾ by being placed first, as you have learned, and were it placed after, the mubtadaʾ would remain an unspecified indefinite."},
    {"type": "matn",
     "ar": "(أو) كان (لمتعلقه) بكسر اللام[[١]] أي: كان لمتعلق الخبر التابع له[[٢]] تبعية يمتنع معها تقديمه[[٣]] على الخبر، فلا يرد نحو: «على الله عبده متوكل»",
     "en": "“Or” there is “for what is connected to it (mutaʿalliqihi)”—with a kasra on the lām—that is, there is for what is connected to the khabar, being dependent on it with a dependence that rules out its being placed before the khabar (so the like of “ʿalā Allāhi ʿabduhu mutawakkilun,” “On Allah His servant relies,” does not count against it),"},
    {"type": "matn",
     "ar": "(ضمير) كائن (في) جانب (المبتدإ[[٤]]) راجع إلى ذلك المتعلق؛ إذ لو أخر لزم الإضمار قبل الذكر لفظا ومعنى",
     "en": "“a pronoun” located “in” the part of “the mubtadaʾ” referring back to that connected element; for were it placed after, pronominalization before mention would follow, both in wording and in meaning;"},
    {"type": "matn",
     "ar": "(مثل: «على التمرة مثلها زبدا») فقوله: «مثلها» أي: «مثل التمرة» مبتدأ، وفيه ضمير لمتعلق الخبر، وهو التمرة؛",
     "en": "“as in: ‘On the date is its like in butter’ (ʿalā al-tamrati mithluhā zubdan).” His words “mithluhā,” that is, “the like of the date,” are the mubtadaʾ, and in it is a pronoun belonging to what is connected to the khabar, namely the date;"},
    {"type": "matn",
     "ar": "لأن الخبر وهو قوله: «على التمرة» و«التمرة» متعلق به مثل تعلق الجزء بالكل[[٥]].",
     "en": "because the khabar is his words “ʿalā al-tamrati,” and “al-tamra” is connected to it in the way a part is connected to the whole."},
    {"type": "matn",
     "ar": "(أو كان) الخبر (خبرا عن «أن»[[٦]]) المفتوحة الواقعة مع اسمها وخبرها المؤول بالمفرد مبتدأ؛",
     "en": "“Or” the khabar “is the khabar of ‘anna’”—the [particle] with fatḥa, which together with its noun and its khabar, construed as a single term, occurs as the mubtadaʾ;"},
    {"type": "matn",
     "ar": "إذ في تأخيره خوف لبس[[٧]] «أن» المفتوحة بالمكسورة[[٨]] في التلفظ",
     "en": "for in placing it after there is the fear of confusing “anna” with fatḥa with the one with kasra (inna) in pronunciation…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ويجوز فتحها بناء على أن الخبر هو الفعل المقدر، والفعل متعلق بالمجرور بسبب حرف الجر.",
     "en": "Its fatḥa [mutaʿallaqihi] is also permissible, on the basis that the khabar is the implied verb, and the verb is what the genitive noun is connected to by means of the preposition."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يقل المصنف: «أو لجزء الخبر»، ولم يفسر الشارح المتعلق بالجزء ليشمل مثل: «قرين كل رجل ضيعته»،",
     "en": "The author did not say “or for part of the khabar,” and the commentator did not explain “what is connected” as “the part,” so that it would include the like of “Each man's companion is his estate” (qarīnu kulli rajulin ḍayʿatuhu);"},
    {"type": "pair",
     "ar": "والأخصر الأوضح أن يقول: أي: لمتعلق الخبر الذي يمنع تقديمه عليه.",
     "en": "the more concise and clearer [wording] would be to say: that is, for what is connected to the khabar such that it prevents its being placed before it."},
    {"type": "pair",
     "ar": "وإنما أراد بالتعلق مثل تعلق الجزء بالكل دون تعلق العامل بالمعمول؛",
     "en": "By connection he meant only the like of the connection of a part to the whole, not the connection of a governor to what it governs;"},
    {"type": "pair",
     "ar": "لأن لمتعلق الخبر تعلق العامل بالمعمول ضميرا في المبتدأ في مثل: «على الله عبده متوكل» مع أنه لا يجب تقديم الخبر.",
     "en": "because what is connected to the khabar by the connection of governor to governed has a pronoun in the mubtadaʾ in the like of “ʿalā Allāhi ʿabduhu mutawakkilun,” and yet placing the khabar first is not obligatory."},
    {"type": "pair",
     "ar": "وقد يقال: أراد تعلق الجزء بالكل دون المعمول بالعامل ليشمل مثل: «قرين كل رجل ضيعته»، والفضل للمتقدم.",
     "en": "It may also be said: he meant the connection of a part to the whole, not of the governed to the governor, so that it would include the like of “qarīnu kulli rajulin ḍayʿatuhu”; and the merit belongs to the former [explanation]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما حكم بامتناع تقديمه للزوم تقدم الشيء على نفسه،",
     "en": "He ruled that placing it first is impossible only because it would entail a thing's preceding itself;"},
    {"type": "pair",
     "ar": "فإن الخبر في المثال المذكور «على التمرة»، فلو قدم التمرة عليه لزم ذلك المحذور.",
     "en": "for the khabar in the example mentioned is “ʿalā al-tamrati,” so if “al-tamra” were placed before it, that objectionable consequence would follow."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "نفسه. أما إذا كان في صفته، فلا يجب التقديم نحو: «على التمرة زبد مثلها»؛",
     "en": "[In the mubtadaʾ] itself. If, however, it is in its adjective, placing first is not obligatory, as in: “ʿalā al-tamrati zubdun mithluhā” (on the date is butter like it);"},
    {"type": "pair",
     "ar": "لجواز تأخير الخبر بأن يتوسط بين المبتدأ وصفته لجواز الفصل بين الصفة والموصوف.",
     "en": "because the khabar may be placed after, by coming between the mubtadaʾ and its adjective, since separating the adjective from what it qualifies is permissible."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما لم يجعل الخبر الفعل المقدر، والتعلق من باب تعلق المعمول بعامله لعدم اطراده في مثل: «غلام رجل مثله» إذا جعلت «مثله» مبتدأ.",
     "en": "He did not make the khabar the implied verb, and the connection one of the governed to its governor, only because that does not hold uniformly in the like of “ghulāmu rajulin mithluhu” when you make “mithluhu” the mubtadaʾ."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بشرط ألا يكون «أن» بعد «أما»، نحو: «أما أنك خارج، فلا أصدقه»،",
     "en": "On condition that “anna” does not come after “ammā,” as in: “As for that you are going out, I do not believe it” (ammā annaka khārijun fa-lā uṣaddiquhu);"},
    {"type": "pair",
     "ar": "فإنه لا يجب حينئذ تقديم الخبر لعدم الالتباس؛ لأن الجملة التامة لا تقع بين «أما» وفائها.",
     "en": "for then placing the khabar first is not obligatory, there being no confusion, since a complete sentence does not occur between “ammā” and its fāʾ."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "دون تقديمه، فإنه حينئذ متعين لأن يكون خبرا عن «أن» المفتوحة مع اسمها وخبرها؛",
     "en": "Not in placing it first; for then it is determined to be the khabar of “anna” with fatḥa together with its noun and khabar;"},
    {"type": "pair",
     "ar": "إذ لا يجوز أن يكون مما في حيز «إن» المكسورة معنى لصدارتها، ولا مما في حيز «أن» المفتوحة معنى؛ لأنها موصولة، ولا يجوز تقديم ما في حيز الموصول عليه،",
     "en": "since it cannot belong in meaning to the domain of “inna” with kasra, because of its headship, nor to the domain of “anna” with fatḥa in meaning, because it is a relative [particle], and what lies in the domain of a relative may not be placed before it;"},
    {"type": "pair",
     "ar": "فتعين أن يكون خبرا إما لـ«أن» المفتوحة مع اسمها وخبرها، أو لـ«إن» المكسورة معهما، والثاني باطل؛ لأنها جملة تامة غير مؤولة بمفرد، فتعين الأول.",
     "en": "so it is determined that it is the khabar either of “anna” with fatḥa together with its noun and khabar, or of “inna” with kasra together with them; the second is invalid, because that is a complete sentence not construed as a single term; so the first is determined."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لجواز أن يكون المذكور بعدها خبرا آخر لها أو ظرفا لخبرها.",
     "en": "Because what is mentioned after it could be another khabar of it, or an adverbial qualifier of its khabar."},
]
