# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 243 (printed ٢٤٢)."""

PAGE_NUMBER = 243
PRINTED_PAGE = "٢٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[المفعول له]",
     "en": "The Object of Purpose (al-Mafʿūl lahu)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(المفعول له: هو ما فعل لأجله) أي: لقصد تحصيله، أو بسبب وجوده.",
     "en": "(The object of purpose (al-mafʿūl lahu) is that for the sake of which) (an action) (is done), that is, with the aim of obtaining it, or because of its existence."},
    {"type": "matn",
     "ar": "وخرج به سائر المفاعيل مما فعل مطلقا، أو به، أو فيه، أو معه",
     "en": "By this are excluded the other objects: that which is done absolutely (the absolute object), or done to, or in, or along with."},
    {"type": "matn",
     "ar": "(فعل[[١]]) أي: حدث (مذكور) أي: ملفوظ حقيقة أو حكما،",
     "en": "(An action), that is, an event, (mentioned), that is, uttered, either actually or in effect (ḥukman);"},
    {"type": "matn",
     "ar": "فلا يخرج عنه ما كان فعله مقدرا، كما إذا قلت: «تأديبا» في جواب من قال: «لم ضربت زيدا».",
     "en": "so what has its verb implied is not excluded from it, as when you say “for discipline” (taʾdīban) in answer to one who says “Why did you strike Zayd?”"},
    {"type": "matn",
     "ar": "فقوله: «مذكور» احتراز عن مثل: «أعجبني التأديب».",
     "en": "His word “mentioned” guards against such a case as “The disciplining pleased me.”"},
    {"type": "matn",
     "ar": "فإن قلت: كيف يصح الاحتراز به عنه، وهو أي: الفعل الذي فعل لأجله مذكور في الجملة كما في «ضربت زيدا؟»",
     "en": "If you say: how is it correct to guard against it by this, when it, that is, the action done for its sake, is mentioned in some way, as in “I struck Zayd”?"},
    {"type": "matn",
     "ar": "قلنا: المراد مذكور معه.",
     "en": "We say: what is meant is “mentioned together with it.”"},
    {"type": "matn",
     "ar": "فإن قلت: هو مذكور معه في «ضربته تأديبا؟».",
     "en": "If you say: it is mentioned together with it in “I struck him for discipline”?"},
    {"type": "matn",
     "ar": "قلنا: المراد مذكور معه في التركيب الذي هو فيه،",
     "en": "We say: what is meant is “mentioned together with it in the construction in which it occurs.”"},
    {"type": "matn",
     "ar": "ويرد حينئذ نحو: «أعجبني التأديب الذي ضربت لأجله»[[٢]]، اللهم إلا أن يراد بذكره معه[[٣]] إيراده معه للعمل فيه[[٤]].",
     "en": "Then such a case as “The disciplining for whose sake I struck pleased me” is an objection, unless by its being mentioned with it is meant its being brought together with it in order to govern it."},
    {"type": "matn",
     "ar": "(مثل: «ضربته تأديبا له»[[٥]]) مثال لما فعل لقصد تحصيله فعل، وهو الضرب، فإن",
     "en": "(For example: “I struck him to discipline him”) is an example of that for the purpose of obtaining which an action, namely striking, is done; for…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: ما هو حامل على الفعل، وهو مقدم إما بحسب التصور أو بحسب التحقق.",
     "en": "That is: what prompts the action; it is prior either in conception or in realization."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بل يرد «أعجبني التأديب»؛ لأنه يصدق عليه أنه ما فعل لأجله الفعل المذكور معه في التركيب الذي هو فيه في قوله: أعجبني التأديب الذي ضربت لأجله.",
     "en": "Rather, “The disciplining pleased me” is an objection, because it is true of it that it is that for whose sake was done the action mentioned with it in the construction in which it occurs, in his words: “The disciplining for whose sake I struck pleased me.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يقال: يخرج مفعول له المجرور، نحو: جئتك للسمن؛ لأن العامل في المجرور هو الجار لا الفعل؛",
     "en": "It is not to be said that the object of purpose in the genitive is excluded, as in “I came to you for the butter (li-l-saman),” because what governs the genitive is the preposition, not the verb;"},
    {"type": "pair",
     "ar": "لأن التحقيق أن العامل في المجرور هو الفعل، وأنه المنصوب محلا، والجار بمنزلة الهمزة والتضعيف.",
     "en": "for the verified view is that what governs the genitive is the verb, that it is accusative in position (maḥallan), and that the preposition is like the hamza [of the fourth form] and the doubling [of the second form]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن تعريف المفعول له ليعرف حكمه، وهو انتصابه بالفعل،",
     "en": "Against this: the object of purpose is defined so that its rule may be known, namely its taking the accusative by the verb;"},
    {"type": "pair",
     "ar": "فلو توقف معرفته على أنه ينتصب بالفعل، وأورد الفعل لينصبه لدار.",
     "en": "so if knowing it depended on its being put in the accusative by the verb, and on the verb being brought in order to put it in the accusative, there would be circularity."},
    # REVIEW: «بعد أعجبني» printed; sense expects «نحو»; transcribed as printed.
    {"type": "pair",
     "ar": "وفيه أيضا أنه يرد عليه بعد أعجبني التأديب الذي ضربت لأجله، بل أعجبني التأديب أيضا؛",
     "en": "Against it also: there is still an objection to it from “The disciplining for whose sake I struck pleased me,” and even from “The disciplining pleased me”;"},
    {"type": "pair",
     "ar": "لأنه يصدق على التأديب أنه ما فعل لأجله فعل مذكور معه للعمل فيه في تركيب «ضربت زيدا للتأديب» فافهم.",
     "en": "for it is true of “disciplining” that it is that for whose sake an action is done which is mentioned with it so as to govern it, in the construction “I struck Zayd for the disciplining.” So understand."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إلى قوله: فإن التأديب إنما يحصل بالضرب.",
     "en": "Up to his words: “for disciplining is obtained only by striking.”"},
    {"type": "pair",
     "ar": "قيل: التأديب عين الضرب، فكيف يحصل به؟",
     "en": "It has been said: disciplining is the very striking, so how can it be obtained by it?"},
    {"type": "pair",
     "ar": "وأجيب: بأنه يحصل به ما يتضمنه التأديب وهو التأدب.",
     "en": "It was answered that what is obtained by it is what disciplining entails, namely becoming disciplined (taʾaddub)."},
    {"type": "pair",
     "ar": "وإنما نصب التأديب لتضمنه التأدب، ويكذبه امتناع \"ضربته تأدبا\"، كما صرح به الرضي ناقلا عن النحاة،",
     "en": "[On this answer] “disciplining” is put in the accusative only because it entails becoming disciplined; but this is belied by the inadmissibility of “I struck him for [his] becoming disciplined (taʾadduban),” as al-Raḍī stated explicitly, reporting it from the grammarians."},
    {"type": "pair",
     "ar": "فالجواب منع أن التأديب عين الضرب، بل هو إحداث التأدب، والضرب سبب الإحداث ووسيلته.",
     "en": "So the answer is to deny that disciplining is the very striking; rather, it is bringing about the state of being disciplined, and striking is the cause and means of that bringing about."},
]
