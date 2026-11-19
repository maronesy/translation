# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 215 (printed ٢١٤)."""

PAGE_NUMBER = 215
PRINTED_PAGE = "٢١٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "ويكون المنادى[[١]] المضاف إلى ياء المتكلم (بالهاء) في هذه الوجوه كلها (وقفا[[٢]]) أي: في حالة الوقف،",
     "en": "The vocative annexed to the yāʾ of the speaker is [pronounced] (with the hāʾ) in all these forms (in pause—waqfan), that is, in the state of pause;"},
    {"type": "matn",
     "ar": "تقول: «يا غلاميه، ويا غلاميه، ويا غلامه، ويا غلاماه» فرقا بين الوقف والوصل.",
     "en": "you say: “yā ghulāmiyah, yā ghulāmīh, yā ghulāmih, yā ghulāmāh,” to distinguish between pause and continuous speech (waṣl)."},
    {"type": "matn",
     "ar": "(وقالوا) أي: العرب في محاوراتهم («يا أبي» و«يا أمي») على الوجوه الأربعة، كسائر ما أضيف إلى ياء المتكلم مع وجوه أخر زائدة عليها، لكثرة استعمال ندائهما في كلامهم،",
     "en": "(And they said)—that is, the Arabs in their conversation—(“yā abī” [O my father] and “yā ummī” [O my mother]) in the four forms, like everything else annexed to the yāʾ of the speaker, together with further forms in addition to these, because calling on these two is so frequent in their speech;"},
    # REVIEW: print reads «فقوله»; probably «بقوله»; transcribed as printed.
    {"type": "matn",
     "ar": "كما أشار إليها فقوله: (ويا أبت ويا أمت معا) أي: قالوا: «يا أبت ويا أمت» أيضا بإبدال الياء بالتاء[[٣]]",
     "en": "as he alluded to them in his words: (and “yā abati” and “yā ummati” together), that is: they also said “yā abati” and “yā ummati,” replacing the yāʾ with the tāʾ,"},
    {"type": "matn",
     "ar": "(فتحا وكسرا) أي: حال كون التاء مفتوحة على وفق حركة الياء أو مكسورة لمناسبة الياء[[٤]].",
     "en": "(with fatḥa and with kasra), that is, the tāʾ being given a fatḥa in accordance with the vowel of the yāʾ, or a kasra because of its affinity with the yāʾ."},
    {"type": "matn",
     "ar": "وقد جاء بالضم أيضا نحو: «يا أبت ويا أمت»؛ لإجرائه مجرى المفرد المعرفة، ولم يذكره للقلة.",
     "en": "It has also come with ḍamma, as in “yā abatu” and “yā ummatu,” because it is treated like the definite single noun; he did not mention it because it is rare."},
    {"type": "matn",
     "ar": "(و) قالوا: «يا أبتا ويا أمتا» (بالألف[[٥]]) بعد التاء جمعا بين العوضين (دون الياء) فما قالوا: «يا أبتي ويا أمتي» احترازا عن الجمع بين العوض والمعوض عنه، فإنه غير جائز.",
     "en": "(And) they said “yā abatā” and “yā ummatā” (with the alif) after the tāʾ, combining the two substitutes, (not with the yāʾ): they did not say “yā abatī” and “yā ummatī,” avoiding the combination of the substitute and what it replaces, which is not permitted."},
    {"type": "matn",
     "ar": "(و) قالوا: («يا ابن أم» و«يا ابن عم» خاصة) هذا الاختصاص بالنظر إلى الأم والعم، أي: لا يقال: «يا ابن أخي، ويا ابن خالي» لا بالنظر إلى الابن أيضا،",
     "en": "(And) they said (“yā ibna umma” [O son of my mother] and “yā ibna ʿamma” [O son of my paternal uncle] specifically). This restriction concerns “mother” and “paternal uncle”—that is, one does not say [this way] “yā ibna akhī” or “yā ibna khālī”—not “son” as well;"},
    {"type": "matn",
     "ar": "فإنهم يقولون: «يا بنت أم، ويا بنت عم» على الوجوه الأربعة (مثل: باب «يا غلامي») فقالوا: «يا ابن أمي، ويا ابن عمي» بفتح الياء وسكونها[[٦]].",
     "en": "for they say “yā binta umma” and “yā binta ʿamma.” [They are used] in the four forms (like the pattern of “yā ghulāmī”): so they said “yā ibna ummī” and “yā ibna ʿammī,” with the yāʾ given a fatḥa or quiescent."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن الباء في قوله: «بالهاء» للملابسة والظرفية معطوفة على الفعلية الواقعة خبرا.",
     "en": "He means that the bāʾ in his words “bi-l-hāʾ” denotes accompaniment and circumstance, [the phrase] being conjoined to the verbal sentence that stands as a predicate."},
    {"type": "pair",
     "ar": "وقوله: وقفا إما حال أو ظرف. ولك أن تقدر فعلا معطوفا على الفعلية، أي: يوقف بالهاء وقفا.",
     "en": "His words “waqfan” are either a ḥāl or an adverbial (ẓarf). You may also supply a verb conjoined to the verbal sentence, that is: “one pauses with the hāʾ, a pausing.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: إذا وقفت على يا غلاما فبالهاء لبيان الوقف،",
     "en": "Shaykh al-Raḍī said: when you pause on “yā ghulāmā,” it is with the hāʾ, to make the pause clear;"},
    {"type": "pair",
     "ar": "وإذا وقفت على يا غلامي بسكون الياء وصلا، فالوقف عليها بالسكون أجود.",
     "en": "and when you pause on “yā ghulāmī,” with the yāʾ quiescent in continuous speech, pausing on it with sukūn is better."},
    {"type": "pair",
     "ar": "ويجوز حذفها وإسكان ما قبلها كما تقف على ما حذف ياؤه وصلا. وذلك على مذهب من وقف على القاضي بإسكان الضاد،",
     "en": "It is also permitted to drop it and make what precedes it quiescent, as you pause on a word whose yāʾ is dropped in continuous speech; this is according to the practice of those who pause on “al-qāḍī” with the ḍād quiescent."},
    {"type": "pair",
     "ar": "وإذا وقفت على يا غلامي بفتح الياء وصلا جاز الإسكان للوقف، وجاز إلحاق هاء السكت مع إبقاء الفتح.",
     "en": "And when you pause on “yā ghulāmiya,” with the yāʾ given a fatḥa in continuous speech, the sukūn is permitted for the pause, and appending the hāʾ of silence (hāʾ al-sakt) while keeping the fatḥa is permitted."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الباء صلة الإبدال. وإنما تدخل على المتروك فهو التحتانية، وما فوقها الفوقانية دون العكس كما سبق الأوهام.",
     "en": "The bāʾ is the complement of ibdāl (replacement). It enters only on what is given up, which is the yāʾ (al-taḥtāniyya), while what is above it is the tāʾ (al-fawqāniyya), not the reverse, as [some] imaginings run ahead to suppose."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن الكسرة حركة مناسبة للحرف المبدل منه، فيكون في المبدل شائبة من المبدل منه.",
     "en": "He means that the kasra is a vowel suited to the letter replaced, so that there is in the replacement a trace of what it replaces."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "عطف بحسب المعنى على \"يا أبت\"، فإن قولنا: وبالألف في معنى و\"يا أبتا\"، فيعطف على\"يا أبت\"،",
     "en": "It is conjoined in meaning to “yā abati,” for our saying “and with the alif” has the sense of “and yā abatā”; so it is conjoined to “yā abati.”"},
    {"type": "pair",
     "ar": "أو عطف على فتحا وكسرا أي: وكائنة بالألف، أو عطف على محذوف أي: بلا ألف،",
     "en": "Or it is conjoined to “fatḥan wa-kasran,” that is: “and being with the alif”; or it is conjoined to something elided, that is: “without the alif,”"},
    {"type": "pair",
     "ar": "والتقدير: قالوا: يا أبت ويا أمت بلا ألف وبالألف، فتأمل.",
     "en": "the implied sense being: they said “yā abati” and “yā ummati” without the alif and with the alif. Reflect on this."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وقالوا أيضا: بالهاء وقفا، فالأولى الإشارة إليه أيضا.",
     "en": "They also said [these] with the hāʾ in pause, so it would have been better to point to that as well."},
]
