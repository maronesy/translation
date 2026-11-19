# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 407 (printed ٤٠٦)."""

PAGE_NUMBER = 407
PRINTED_PAGE = "٤٠٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «...فالملحوظ في الظرفية أولا الزمان الدال عليه الألفاظ الموضوعة للزمان، وفي المصدرية أولا الحديث» at the foot of PDF p. 406.
    {"type": "matn",
     "ar": "الدال عليه لفظ المصدر، ويحتمل أن يكون المثال الثاني بتقدير: «كم رجلا أو رجل ضربت»، فعلى هذا التقدير يكون «كم» منصوبا على المفعولية.",
     "en": "…that the expression of the maṣdar signifies. The second example may also be taken as supposing “kam rajulan” or “kam rajulin ḍarabta” (how many men did you strike / how many a man you struck); on this supposition “kam” is in the accusative as a direct object."},

    {"type": "section", "ar": "[الظروف]",
     "en": "Adverbs of Time and Place (al-Ẓurūf)"},

    {"type": "matn",
     "ar": "(الظروف) أي: الظروف المعدودة من المبنيات المعبر عنها عند تعدادها ببعض الظروف، فلا حاجة إلى ذكر البعض ههنا[[١]].",
     "en": "(The adverbs) (al-ẓurūf), that is, the adverbs counted among the indeclinables, which were expressed, when they were enumerated, as “some adverbs”; so there is no need to mention “some” here."},
    {"type": "matn",
     "ar": "(منها) أي: من تلك الظروف (ما) أي: ظرف[[٢]] (قطع عن الإضافة) بحذف المضاف إليه عن اللفظ دون النية،",
     "en": "(Among them), that is, among those adverbs, is (what), that is, an adverb (that is cut off from annexation (iḍāfa)), by the omission of the annexed noun from the wording but not from the intention;"},
    {"type": "matn",
     "ar": "فإنه عند نسيانه أعرب مع التنوين نحو: «رب بعد كان خيرا من قبل»،",
     "en": "for when it is forgotten [altogether], [the adverb] is declined with nunation, as in “rubba baʿdin kāna khayran min qablin” (many an afterwards has been better than a before)."},
    {"type": "matn",
     "ar": "وسميت الظروف المقطوعة عن الإضافة غايات؛ لأن غاية الكلام[[٣]] كانت ما أضيفت هي إليه[[٤]]، فلما حذف صرن غايات ينتهي بها الكلام،",
     "en": "The adverbs cut off from annexation are called “ghāyāt” (end-points), because the end of the utterance was that to which they were annexed; when it was omitted, they became end-points at which the utterance terminates."},
    {"type": "matn",
     "ar": "وإنما بنيت لتضمنها معنى حرف الإضافة[[٥]]، وشبهها بالحروف في الاحتياج إلى المضاف إليه، واختير الضم، لجبر النقصان",
     "en": "They are indeclinable only because they contain the meaning of the particle of annexation and resemble particles in needing the annexed noun; and the ḍamma was chosen to make up for the deficiency,"},
    {"type": "matn",
     "ar": "(كـ«قبل» و«بعد») وما أشبههما من الظروف المسموع قطعها عن الإضافة، مثل: «تحت، وفوق، وقدام، وخلف، ووراء»، ولا يقاس عليها ما بمعناها،",
     "en": "(like “qablu” and “baʿdu”) and the adverbs resembling them whose being cut off from annexation is attested, such as “taḥtu, fawqu, quddāmu, khalfu, warāʾu”; what has their meaning is not formed on their analogy."},
    {"type": "matn",
     "ar": "ويجوز في هذه الظروف على قلة أن يعوض التنوين من المضاف إليه فيعرب، قال:",
     "en": "In these adverbs it is permitted, rarely, that nunation be substituted for the annexed noun, so that the adverb is declined. [The poet] said:"},
    {"type": "verse",
     "ar": "فساغ[[٦]] لي الشراب وكنت قبلا          أكاد أغص[[٧]] بالماء الفرات",
     "en": "Then drink became easy for me to swallow, whereas before / I would almost choke on sweet water."},
    {"type": "matn",
     "ar": "فلا فرق بين ما أعرب من هذه الظروف المقطوعة وبين ما بني منها.",
     "en": "So there is no difference [in meaning] between those of these cut-off adverbs that are declined and those that are indeclinable."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: حذف؛ لأن اللام يغني غناءه، فيكون ذكره ذكرا لما لا حاجة إليه،",
     "en": "He means: it was omitted because the definite article (lām) does its work, so mentioning it would be mentioning what is not needed."},
    {"type": "pair",
     "ar": "ولك أن تقول: حذف إزالة لإبهام كون بعض الظروف اسما كاسم الإشارة.",
     "en": "You may also say: it was omitted to remove the suggestion that “some adverbs” is a name, like a demonstrative noun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل «ما» بمعنى الظرف بقرينة قوله: الظروف.",
     "en": "He took “mā” in the sense of “adverb” on the evidence of his word “the adverbs”."},
    {"type": "pair",
     "ar": "ولك أن تبقيه على عمومه إشارة إلى أن من الظروف في باب المبني ما قطع عن الإضافة من كل وجه حتى لم يبق أثر من الإضافة، كما فيما عوض عن المضاف إليه شيء،",
     "en": "You may also leave it in its generality, as an indication that among the adverbs in the chapter of the indeclinable is one cut off from annexation in every respect, so that no trace of annexation remains, as in that for whose annexed noun something has been substituted;"},
    {"type": "pair",
     "ar": "فإنه حينئذ كأنه لا قطع، فيدخل في الظروف ما أجري مجراه.",
     "en": "for then it is as though there were no cutting off, and so what is treated like it enters among the adverbs."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في قصد المتكلم.",
     "en": "That is, in the speaker’s intention."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن غاية الكلام في كل أمر نسبي يجب أن يكون المنسوب إليه، أو غاية الكلام فيما قصد إضافته يجب أن يكون المضاف إليه.",
     "en": "Because the end of the utterance in every relational matter must be that to which it is related; or, the end of the utterance in what is intended to be annexed must be the annexed noun."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لتضمنها معنى المضاف إليه، كذا في شرح المفصل.",
     "en": "Because they contain the meaning of the annexed noun; so in Sharḥ al-Mufaṣṣal."},
    {"type": "pair",
     "ar": "فليس حرف الجر ههنا مقدرا كما في «غلام زيد»، بل مفهوما معناه من الغاية، فيفهم المضاف إليه منها من حيث إنه مضاف إليه.",
     "en": "So the preposition is not supposed here, as it is in “ghulāmu Zaydin” (Zayd’s servant); rather its meaning is understood from the end-point, so the annexed noun is understood from them as annexed noun."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: سهل مدخله، كذا في القاموس.",
     "en": "That is, its passage became easy; so in al-Qāmūs."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "من باب علم، أو فتح على ما في القاموس.",
     "en": "Of the pattern of ʿalima, or of fataḥa, according to al-Qāmūs."},
]
