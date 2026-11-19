# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 354 (printed ٣٥٣)."""

PAGE_NUMBER = 354
PRINTED_PAGE = "٣٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أي: كل ما خالف حكمه إذا كان عطف بيان حكمه إذا كان» at the foot of PDF p. 353.
    {"type": "matn",
     "ar": "بدلا، فيتناول صورة النداء أيضا،",
     "en": "…a substitute; so it also covers the case of the vocative."},
    {"type": "matn",
     "ar": "فإنك تقول: «يا غلام زيد وزيدا» بالتنوين مرفوعا، حملا على اللفظ، ومنصوبا حملا على المحل إذا جعلته عطف بيان،",
     "en": "For you say “yā ghulāmu Zaydun” and “Zaydan”, with nunation—in the nominative, construed with the wording, and in the accusative, construed with the [grammatical] position—when you make it an explicative apposition,"},
    {"type": "matn",
     "ar": "و«يا غلام زيد» -بالضم- إذا جعلته بدلا، والمعنى الأول أظهر، والثاني أفيد.",
     "en": "and “yā ghulāmu Zaydu”, with ḍamma [and no nunation], when you make it a substitute. The first sense is more apparent, and the second more informative."},

    {"type": "section", "ar": "[المبني]",
     "en": "The Indeclinable Noun (al-Mabnī)"},

    {"type": "matn",
     "ar": "(المبني) أي: الاسم المبني،",
     "en": "(The indeclinable) (al-mabnī), that is, the indeclinable noun."},
    {"type": "matn",
     "ar": "وهذا الحد لا يصح إلا لمن يعرف ماهية المبني على الإطلاق[[١]]، ولا يعرف الاسم المبني؛",
     "en": "This definition is sound only for one who knows the quiddity of the indeclinable without qualification, and does not know the indeclinable noun;"},
    {"type": "matn",
     "ar": "إذ لو لم يعرفها[[٢]] لكان تعريفا للمبني بالمبني؛ لأنه ذكر في حد المبني لفظ المبني[[٣]]",
     "en": "for if he did not know it, this would be a definition of the indeclinable by the indeclinable, since the word “indeclinable” is mentioned in the definition of the indeclinable."},
    {"type": "matn",
     "ar": "(ما ناسب) أي: اسم ناسب (مبني الأصل) وهو: الحرف، والفعل الماضي[[٤]]، والأمر بغير اللام[[٥]].",
     "en": "(That which bears a resemblance), that is, a noun that bears a resemblance (to what is indeclinable by origin) (mabnī al-aṣl), namely the particle, the past-tense verb, and the imperative without the lām."},
    {"type": "matn",
     "ar": "والمراد بالمشابهة المنفية في تعريف المعرب هو هذه المناسبة[[٦]].",
     "en": "What is meant by the resemblance negated in the definition of the declinable (muʿrab) is this resemblance (munāsaba)."},
    {"type": "matn",
     "ar": "ولقد فصل[[٧]] صاحب المفصل هذه المناسبة بأنها إما بتضمن الاسم معنى مبني",
     "en": "The author of al-Mufaṣṣal set out this resemblance in detail: it consists either in the noun’s including the meaning of something indeclinable…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: هذا الحد للاسم المبني كما هو الظاهر بعد قوله: أي: الاسم المبني،",
     "en": "That is, this definition is of the indeclinable noun, as is apparent after his words “that is, the indeclinable noun”."},
    {"type": "pair",
     "ar": "فهذا إنما يتم لو كان معرفة مبني الأصل موقوفا على معرفة المبني والأصل لكنه ممنوع؛",
     "en": "This would hold only if knowledge of “what is indeclinable by origin” depended on knowledge of “the indeclinable” and “origin”; but that is denied,"},
    {"type": "pair",
     "ar": "لأنه يمكن معرفته بما بينه فيما بعد من غير توقف على معرفة مفهوم المركب الإضافي.",
     "en": "because it can be known through what he explains afterwards, without depending on knowledge of the concept of the genitive compound."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: لو لم يعرف ماهية المبني لكان، أي: تعريف الاسم المبني تعريفا للمبني بالمبني، فيلزم تعريف الشيء بنفسه، هذا محصل كلامه،",
     "en": "He means: if he did not know the quiddity of the indeclinable, it—that is, the definition of the indeclinable noun—would be a definition of the indeclinable by the indeclinable, and it would follow that a thing is defined by itself. This is the gist of his words."},
    # REVIEW: «بنتفسه» printed (clearly a misprint for «بنفسه»); transcribed as printed.
    {"type": "pair",
     "ar": "وفيه نظر؛ لأن لزوم تعريف الشيء بنتفسه لو سلم إنما يلزم لو كان تعريفا للمبني المطلق.",
     "en": "This is open to question, because the consequence of defining a thing by itself, if granted, follows only if it were a definition of the indeclinable without qualification."},
    {"type": "pair",
     "ar": "وأما إذا كان تعريفا للاسم المبني، فليس إلا تعريف الخاص بالعام، ولا محذور فيه،",
     "en": "But if it is a definition of the indeclinable noun, it is nothing but the definition of the specific by the general, and there is nothing objectionable in that."},
    {"type": "pair",
     "ar": "نعم لو كان تعريف المبني المطلق يلزم ألا يكون جامعا لخروج مبني الأصل؛ لأنه لا يناسب مبني الأصل.",
     "en": "Admittedly, were it a definition of the indeclinable without qualification, it would follow that it is not comprehensive, since what is indeclinable by origin would be left out, for it does not resemble what is indeclinable by origin."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يقال: جاز أن يكون المبني المأخوذ في التعريف معلوما بوجه غير الوجه الذي أريد كسبه؛",
     "en": "It should not be said: the “indeclinable” taken in the definition may be known in a respect other than the respect that is meant to be acquired;"},
    {"type": "pair",
     "ar": "لأنا نقول: لا اعتبار لهذا الاحتمال، وإلا لم يصح الاعتراض على تعريفه بأنه تعريف الشيء بنفسه.",
     "en": "for we say: this possibility is of no account; otherwise the objection to his definition that it defines a thing by itself would not be sound."},
    {"type": "pair",
     "ar": "والظاهر أن السر في ذلك أن اللفظ حقيقة في مسماه مجاز في غيره؛ فلو أريد به وجهه لا مفهومه كان مجازا.",
     "en": "The apparent reason for this is that a word is literal (ḥaqīqa) in what it names and figurative (majāz) in anything else; so if one of its aspects, not its concept, were meant by it, it would be figurative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يبين مفهوم المركب الإضافي، واكتفى بتعيين ما يصدق عليه؛ لأنه سبق معرفة مفهومه في تعريف المعرب،",
     "en": "He did not explain the concept of the genitive compound, and was content to specify what it applies to, because knowledge of its concept preceded in the definition of the declinable."},
    {"type": "pair",
     "ar": "ولا حاجة إلى تقييد الأمر بقوله: بغير اللام؛ إذ لا أمر في عرف النحاة إلا بغير اللام.",
     "en": "There is no need to restrict the imperative with his words “without the lām”, since in the usage of the grammarians there is no imperative except without the lām."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يقل: وأمر المخاطب كما هو المشهور؛ لأن أمر المخاطب إذا كان مع اللام كان معربا.",
     "en": "He did not say “and the imperative of the second person”, as is commonly said, because the imperative of the second person, when it is with the lām, is declinable."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى هو المناسبة فافهم.",
     "en": "It would have been better [to say] “it is the resemblance”. So understand."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: أنه أراد بقوله: ما ناسب مبني الأصل مناسبة معتبرة تفصيلها ما ذكره صاحب المفصل،",
     "en": "He means: by his words “that which bears a resemblance to what is indeclinable by origin” he meant a recognized resemblance, whose detailed account is what the author of al-Mufaṣṣal mentioned;"},
    {"type": "pair",
     "ar": "لكن يشترط ألا يعارض جهة مقتضية للإعراب كإضافة «أي» الموصولة.",
     "en": "but it is a condition that no aspect requiring inflection oppose it, such as the annexation of the relative “ayy”."},
    {"type": "pair",
     "ar": "وبهذا التحقيق اندفع ما يتجه عليه من أنه لا يجوز أن يراد مطلق المناسبة لظهور بطلانه،",
     "en": "By this verification the objection raised against him is removed: that unqualified resemblance cannot be meant, since its invalidity is evident;"},
    {"type": "pair",
     "ar": "ولا مناسبة مؤثرة للبناء لاستلزامه الدور،",
     "en": "nor a resemblance that brings about indeclinability, since that entails circularity;"},
    {"type": "pair",
     "ar": "ولا مناسبة قوية لاستلزامه التعريف بالمجهول؛ لأن للقوة مراتب. ولا يراد بها معنى شامل لجميع تلك المراتب.",
     "en": "nor a strong resemblance, since that entails definition by the unknown, for strength has degrees, and no sense covering all those degrees is meant by it."},
]
