# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 91 (printed ٩٠)."""

PAGE_NUMBER = 91
PRINTED_PAGE = "٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فإنه لو قال: «بأحمد» لا يخل بالوزن، ولكنه يخل بالقافية، فإن حرف الروي في سائر الأبيات الدال المكسورة.",
     "en": "For were he to say “bi-Aḥmad,” it would not disrupt the metre, but it would disrupt the rhyme, since the rhyme-letter (rawī) in the rest of the verses is the kasra-bearing dāl."},

    {"type": "matn",
     "ar": "(أو للتناسب) أي: ويجوز صرف غير المنصرف، ليحصل التناسب بينه وبين المنصرف؛",
     "en": "(Or for the sake of correspondence) — that is: it is permissible to give the diptote (ghayr al-munṣarif) full triptote inflection (ṣarf), so that correspondence (tanāsub) may be achieved between it and the fully-declinable triptote (munṣarif);"},

    {"type": "matn",
     "ar": "لأن رعاية التناسب بين الكلمات أمر مهم عندهم، وإن لم يصل إلى حد الضرورة.",
     "en": "because observing correspondence between words is an important matter with them, even if it does not rise to the level of poetic necessity (ḍarūra)."},

    {"type": "matn",
     "ar": "(مثل ﴿سلاسلا وأغلالا﴾[[١]]) حيث صرف «سلاسلا»[[٢]] لتناسب المنصرف الذي يليه[[٣]]، أعني: «أغلالا»،",
     "en": "(As in “salāsilā wa-aghlālā”) — where “salāsilā” was given full inflection so as to correspond with the triptote that follows it, namely “aghlālā”;"},

    {"type": "matn",
     "ar": "فقوله: «سلاسلا وأغلالا» مثال لمجموع غير المنصرف[[٤]] الذي صرف، والمنصرف الذي صرف غير المنصرف لتناسبه.",
     "en": "so his words “salāsilā wa-aghlālā” are an example encompassing both the diptote that was fully inflected and the triptote for correspondence with which the diptote was inflected."},

    {"type": "matn",
     "ar": "(وما يقوم مقامهما[[٥]]) أي: العلة الواحدة[[٦]] التي تقوم مقام العلتين من العلل التسع،",
     "en": "(And that which stands in the place of the two of them) — that is: the single cause (ʿilla) that stands in the place of two causes among the nine causes,"},

    {"type": "matn",
     "ar": "علتان مكررتان قامت كل واحدة منها مقام العلتين لتكررهما:",
     "en": "[these are] two reduplicated causes, each of which stands in the place of two causes on account of its reduplication:"},

    {"type": "matn",
     "ar": "إحداهما: (الجمع) البالغ إلى صيغة منتهى الجموع[[٧]]، فإنه قد تكرر فيه الجمعية حقيقة، ك«أكالب» و«أساور» و«أناعيم»،",
     "en": "The first of the two is (the plural, al-jamʿ) that reaches the form of the ultimate plural (muntahā al-jumūʿ), for plurality has been reduplicated within it in reality, as in “akālib,” “asāwir,” and “anāʿīm”;"},

    {"type": "matn",
     "ar": "أو حكما كالجموع الموافقة لها في عدد الحروف، والحركات، والسكنات، ك«مساجد» و«مصابيح».",
     "en": "or [reduplicated] by legal ruling (ḥukman), like the plurals that conform to them in the number of letters, vowels, and quiescences, such as “masājid” and “maṣābīḥ.”"},

    {"type": "matn",
     "ar": "وثانيهما: التأنيث، لكن لا مطلقا، بل بعض أقسامه (و) هو (ألفا التأنيث[[٨]]) المقصورة والممدودة[[٩]]،",
     "en": "The second of the two is feminization (taʾnīth), yet not absolutely, but rather one of its subdivisions — namely (and it is) (the two alifs of feminization, alifā al-taʾnīth), the shortened (maqṣūra) and the extended (mamdūda);"},

    {"type": "matn",
     "ar": "أي: كل واحدة منها ك«حبلى» و«حمراء»؛ لأنهما لازمتان للكلمة وضعا، لا تفارقانها أصلا،",
     "en": "that is: each of them, as in “ḥublā” and “ḥamrāʾ”; for the two of them are inseparable from the word by original coinage, never parting from it at all,"},

    {"type": "matn",
     "ar": "فلا يقال في «حبلى»: حبل، ولا «حمراء»: حمر، فيجعل...",
     "en": "so that one does not say “ḥubl” for “ḥublā,” nor “ḥumr” for “ḥamrāʾ,” and so [the alif of feminization] is made [to be...]"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "على قراءة نافع والكسائي وأبي بكر.",
     "en": "According to the reading of Nāfiʿ, al-Kisāʾī, and Abū Bakr."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "تعليل لصحة التمثيل به، أو للمكان إشارة إلى قراءة أخرى بدون رعاية التناسب.",
     "en": "A justification for the soundness of citing it as an example; or there is room [in it] for an allusion to another reading in which correspondence is not observed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا في خصوص المادة، وإلا فقد يكون المنصرف الذي يجعل الغير المنصرف مناسبا له في كلام آخر مقدما عليه أو مؤخرا عنه، كما صرف «قوارير» لرعاية فواصل الآيات.",
     "en": "This applies only to this particular instance; otherwise the triptote for correspondence with which the diptote is made suitable may, in other speech, come before it or after it, just as “qawārīr” was fully inflected to observe the verse-endings (fawāṣil) of the āyāt."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الغير المنصرف الذي وقع في التركيب وكلام الفصيح.",
     "en": "That is: the diptote which occurred in the [poetic] construction and in the eloquent speech [of the Arabs]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اللائق تقديمه على الحكم؛ لأنه بصدد بيان ما أبهمه في «أو» غير المنصرف.",
     "en": "It would have been more fitting to place it before the ruling, for it is engaged in clarifying what he had left ambiguous in the “or” [clause] of [the definition of] the diptote."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يشير إلى أن هذا مما أجمله المصنف في تعريف غير المنصرف حيث قال فيه: «أو واحدة منها تقوم» إلى آخره، وإلى أن «ما» موصولة، وأن الموصول للعهد حيث قال: من العلل التسع.",
     "en": "He indicates that this is among what the author stated summarily in his definition of the diptote, where he said therein: “or one of them that stands [in place of two],” to the end [of the phrase]; and [he indicates] that the “mā” is a relative pronoun, and that the relative refers to a known referent (ʿahd), where he said: “among the nine causes.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "زاد لفظ الصيغة؛ لأن «مساجد» مثلا ليس منتهى الجموع، بل على صيغته ووزنه، يعني: أن كونه على تلك الصيغة يقوي شبه الجمعية، بخلاف الصفة مثلا.",
     "en": "He added the word “form” (ṣīgha) because “masājid,” for instance, is not [itself] an ultimate plural, but is [merely] upon its form and pattern; meaning that its being upon that form strengthens the resemblance to plurality — unlike an adjective (ṣifa), for example."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فيه مسامحة. والمراد التأنيث الواقع بسبب إحداهما.",
     "en": "In this there is a loose usage (musāmaḥa); what is intended is the feminization that occurs by reason of one of the two [alifs]."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الهمزة في الممدودة مقلبة عن الألف، وهي للتأنيث دون الألف التي قبلها. ولما لم يفارق إحداهما الأخرى نسبنا التأنيث تغليبا.",
     "en": "The hamza in the extended [alif] (mamdūda) is converted from an alif, and it is the one that serves feminization, not the alif before it. And since neither of the two ever parts from the other, we ascribed the feminization [to both jointly] by way of predominance (taghlīb)."},
]
