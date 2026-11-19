# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 194 (printed ١٩٣)."""

PAGE_NUMBER = 194
PRINTED_PAGE = "١٩٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from page 193 ("…من حيث إنه")
    {"type": "matn",
     "ar": "منصوص عليه بالمصدر.",
     "en": "…is stated explicitly by the maṣdar."},
    {"type": "matn",
     "ar": "ويحتمل[[١]] أن يكون المراد أنه تأكيد لأجل غيره ليندفع،",
     "en": "It is also possible that what is meant is that it is an emphasis for the sake of something else, so that [that other] may be repelled;"},
    {"type": "matn",
     "ar": "وعلى هذا ينبغي أن يكون المراد بالتأكيد لنفسه أنه تأكيد لأجل نفسه؛ ليتكرر ويتقرر حتى يحسن التقابل.",
     "en": "on this reading, what is meant by “emphasis of itself” should be that it is an emphasis for its own sake, so that it is repeated and made firm, and the contrast [between the two terms] is well balanced."},
    {"type": "matn",
     "ar": "(ومنها: ما وقع مثنى) أي: على صيغة التثنية وإن لم يكن للتثنية[[٢]]، بل للتكرير والتكثير.",
     "en": "(And among them is what occurs as a dual—muthannā), that is, in the form of the dual, even if it is not for duality but for repetition and multiplication."},
    {"type": "matn",
     "ar": "ولا بد في تتميم هذه القاعدة من قيد الإضافة، أي: «مثنى مضافا إلى الفاعل أو المفعول»[[٣]]؛",
     "en": "To complete this rule, the condition of annexation (iḍāfa) is indispensable, that is: “a dual annexed to the agent or the patient”;"},
    {"type": "matn",
     "ar": "لئلا يرد مثل قوله تعالى: ﴿ثم ارجع البصر كرتين﴾[[٤]] أي: رجعا مكررا كثيرا،",
     "en": "so that the like of His words, the Exalted, “Then turn your gaze again, twice” (thumma rjiʿi al-baṣara karratayn) does not count against it, that is: a turning repeated many times."},
    {"type": "matn",
     "ar": "وفي جعل المثال من تتمة التعريف لإفادة هذا القيد تكلف[[٥]].",
     "en": "To make the example part of the completion of the definition so as to convey this condition is strained (takalluf)."},
    {"type": "matn",
     "ar": "(مثل: لبيك) أصله: «ألب[[٦]] لك إلبابين» أي: «أقيم لخدمتك، وامتثال أمرك، ولا أبرح عن مكاني إقامة كثيرة متتالية»،",
     "en": "(Such as labbayka): its origin is “ulibbu laka ilbābayn,” that is: “I stay for your service and the fulfilment of your command, and I do not leave my place—a staying that is abundant and continuous.”"},
    {"type": "matn",
     "ar": "فحذف الفعل[[٧]] وأقيم المصدر مقامه، ورد إلى الثلاثي بحذف زوائده، ثم حذف حرف الجر من المفعول، وأضيف المصدر إليه، فصار «لبيك».",
     "en": "Then the verb was elided and the maṣdar put in its place; it was returned to the triliteral by dropping its augments; then the preposition was dropped from the object and the maṣdar annexed to it, and it became “labbayka.”"},
    {"type": "matn",
     "ar": "ويجوز[[٨]] أن يكون من «لب» بالمكان بمعنى «ألب»، فلا يكون محذوف الزوائد.",
     "en": "It may also be from “labba bi-l-makān” (he stayed in the place) in the sense of “alabba,” so that it is not [a form] with its augments dropped."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إليه ذهب المصنف، وزيف لفوات حسن التقابل؛ لأن اللام في «تأكيدا لنفسه» للصلة لا للأجل،",
     "en": "This is the view the author took, and it has been judged unsound because the balanced contrast is lost; for the lām in “taʾkīdan li-nafsihi” is a connective (li-l-ṣila), not [the lām] of purpose,"},
    {"type": "pair",
     "ar": "اللهم إلا أن يصرف الكلام عن الظاهر، وتجعل للأجل كما قال: وعلى هذا ينبغي إلى آخره.",
     "en": "unless the wording is turned from its apparent sense and [the lām] is taken as one of purpose, as he said: “on this reading, it should…” to the end."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى ترك «إن»؛ لأن عدم إرادة التثنية معتبرة في هذه الضابطة، و«إن» الوصلية لا تفيد ذلك، بل تجتمع بإرادة التثنية أيضا.",
     "en": "It would be better to omit “in” (even if); because the absence of intended duality is a condition in this rule, and concessive “in” (in al-waṣliyya) does not convey that; rather it is compatible with intended duality as well."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال بعض المحققين: ومع هذا القيد ينتقض بـ«ضربت ضربي الأمير»، فإنه مثنى مضافا إلى الفاعل،",
     "en": "One of the verifying scholars said: even with this condition it is contradicted by “ḍarabtu ḍarbayi al-amīr” (I struck the two strikings of the emir), for it is a dual annexed to the agent;"},
    {"type": "pair",
     "ar": "فلا بد أن يقال: مضافا إلى فاعل الفعل أو مفعوله، ومع ذلك ينتقض بـ«ضرب زيد ضربته»،",
     "en": "so one must say: “annexed to the agent of the verb or its patient”; yet even so it is contradicted by “ḍaraba Zaydun ḍarbatayhi” (Zayd struck his two strikings)."},
    {"type": "pair",
     "ar": "فالوجه أن يقيد الإضافة بكونها لا لبيان النوع. وقد صرح بهذا القيد الرضي، انتهى.",
     "en": "The right course is to restrict the annexation to its not being for specifying the kind. Al-Raḍī stated this condition explicitly. [End of quotation.]"},
    {"type": "pair",
     "ar": "ويمكن أن يقال: إنه صرح الشارح بأن المراد بمثنى أن يكون على صيغة التثنية، ولم يكن المراد التثنية، بل التكرير والتكثير،",
     "en": "It may be said: the commentator stated explicitly that what is meant by “dual” is its being in the form of the dual, duality not being meant, but rather repetition and multiplication;"},
    {"type": "pair",
     "ar": "ومع هذا قال: لا بد في تتميم القاعدة من قيد الإضافة، أي: مثنى مضافا،",
     "en": "and with this he said: to complete the rule the condition of annexation is indispensable, that is: “a dual that is annexed.”"},
    {"type": "pair",
     "ar": "فإذا كان مثنى بهذا المعنى لم يرد مواد النقض المذكورة؛ إذ الظاهر أن المعنى على خصوص التثنية لا على التكرير والتكثير، كما لا يخفى.",
     "en": "So if it is a dual in this sense, the counter-instances mentioned do not apply, since the apparent sense [in them] is specifically duality, not repetition and multiplication, as is not hidden."},
    # REVIEW: print reads «ضرب زيد ضربته» (no dual yāʾ); one expects «ضربتيه»; transcribed as printed.

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة الملك: ٤.",
     "en": "Qurʾān, Sūrat al-Mulk 67:4."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إذ الشائع تمام التعريف بدون المثال على أن التقييد بالمثال يفيد ظاهره اشتراط كون المثنى للتكثير، واشتراط الإضافة إلى المفعول.",
     "en": "Since what is customary is that a definition is complete without the example; moreover, restricting by the example would, on its face, convey the conditions that the dual be for multiplication and that it be annexed to the patient."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا ألبي من التلبية؛ لأنها مأخوذة من لبيك.",
     "en": "Not “ulabbī” from talbiya (saying “labbayka”), because that is itself taken from “labbayka.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إلى آخره كل ذلك ليفرغ المجيب بالسرعة من التلبية، فيتفرغ لاستماع المأمور به حتى يمثله.",
     "en": "[His words “the verb was elided”] to the end: all this is so that the one answering may finish the talbiya quickly and be free to listen to what he is commanded, so as to carry it out."},
    # REVIEW: print reads «حتى يمثله»; one expects «يمتثله»; transcribed as printed.

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قيل: أصله لبا، وهو مفرد أضيف إلى الضمير، فقلب ألفه ياء، كلدى أو ليس بشيء لبقاء يائه مضافا إلى المظهر.",
     "en": "It has been said: its origin is “labban,” a singular annexed to the pronoun, whose alif was changed to yāʾ, as with “ladā”; but this is nothing, since its yāʾ remains when it is annexed to an explicit noun."},
]
