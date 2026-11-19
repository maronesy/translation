# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 164 (printed ١٦٣)."""

PAGE_NUMBER = 164
PRINTED_PAGE = "١٦٣"   # Arabic-Indic, as printed

# Note: the first note block below ("num": "") is the continuation of
# footnote ١٠ from the previous page; it carries no marker on this page, so the
# note count is one more than the marker count (9 markers, 9 numbered notes).

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "تقديمه على المبتدأ، لتضمنه معنى الاستفهام.",
     "en": "…to be placed before the mubtadaʾ, because it implicitly contains the meaning of the interrogative."},
    {"type": "matn",
     "ar": "(أو كانا) أي: المبتدأ والخبر (معرفتين[[١]]) متساويين في التعريف أو غير متساويين، ولا قرينة[[٢]] على كون أحدهما مبتدأ والآخر خبرا[[٣]]، نحو: «زيد المنطلق»[[٤]].",
     "en": "“Or [if] the two”—that is, the mubtadaʾ and the khabar—“are definite (maʿrifatayn),” whether equal in definiteness or not equal, and there is no contextual indicator (qarīna) that one of them is the mubtadaʾ and the other the khabar, as in: “Zayd is the one setting off” (Zaydun al-munṭaliqu)."},
    {"type": "matn",
     "ar": "(أو) كانا (متساويين[[٥]]) في أصل التخصيص لا في قدره[[٦]]، حتى لو قيل: «غلام رجل صالح خير منك» لوجب تقديمه أيضا (مثل: «أفضل منك أفضل مني») دفعا للاشتباه[[٧]].",
     "en": "“Or” the two are “equal”—in the basic fact of specification (takhṣīṣ), not in its degree—so that even if it were said, “The slave of a righteous man is better than you,” its placing first would likewise be obligatory; “as in: ‘One more excellent than you is more excellent than I’ (afḍalu minka afḍalu minnī)”—in order to ward off confusion."},
    {"type": "matn",
     "ar": "(أو كان الخبر فعلا له[[٨]]) أي: للمبتدأ، احتراز عما لا يكون فعلا له كما في قولك: «زيد قام أبوه»، فإنه لا يجب فيه تقديم المبتدأ، لجواز أن يقال: «قام أبوه زيد» لعدم الالتباس،",
     "en": "“Or the khabar is a verb belonging to it,” that is, to the mubtadaʾ—a qualification excluding what is not a verb belonging to it, as in your saying, “Zayd, his father stood” (Zaydun qāma abūhu); for in it placing the mubtadaʾ first is not obligatory, since it is permissible to say, “His father stood, Zayd” (qāma abūhu Zaydun), there being no confusion;"},
    {"type": "matn",
     "ar": "(مثل: «زيد قام» وجب تقديمه) أي: تقديم المبتدأ على الخبر في هذه الصور[[٩]].",
     "en": "“as in: ‘Zayd stood’ (Zaydun qāma), its placing first is obligatory”—that is, placing the mubtadaʾ before the khabar in these cases."},
    {"type": "matn",
     "ar": "أما في الصورة الأول، فلما ذكرناه.",
     "en": "As for the first cases, it is for the reason we have mentioned."},
    {"type": "matn",
     "ar": "وأما في الصورة الأخيرة، فلئلا يلتبس المبتدأ بالفاعل إذا كان الفعل مفردا، مثل:",
     "en": "As for the last case, it is so that the mubtadaʾ is not confused with the fāʿil when the verb is singular, as in:…"},

    {"type": "rule"},

    # ---------------- Footnote 10 (continued from previous page) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "للاستفهام أو أفعل التفضيل مقدما على خبره، والجملة صفة لما قبلها نحو: «مررت برجل أفضل منه أبوه».",
     "en": "…[implicitly containing] the interrogative or the elative (afʿal al-tafḍīl), placed before its khabar, the sentence being an adjective qualifying what precedes it, as in: “I passed by a man than whom his father is more excellent” (marartu bi-rajulin afḍalu minhu abūhu)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الضابط في جعل إحداهما مبتدأ والأخرى خبرا: أن ما زعمت أن السامع يطلب العلم بكونه وصفا للأخرى تجعله خبرا.",
     "en": "The rule for making one of the two the mubtadaʾ and the other the khabar is this: whichever you judge the hearer to be seeking knowledge of as a description of the other, you make the khabar."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فلو وجدت قرينة معينة للمراد لم يجب التقديم مثل: «أبو حنيفة أبو يوسف»؛ إذ المقصود تشبيه الثاني بالأول.",
     "en": "So if a contextual indicator specifying what is intended were present, placing [the mubtadaʾ] first would not be obligatory, as in: “Abū Ḥanīfa is Abū Yūsuf,” since what is intended is the likening of the second to the first."},
    {"type": "pair",
     "ar": "ومنه: لعاب الأفاعي القاتلات لعابه.",
     "en": "Of this kind is [the line]: “The saliva of deadly vipers is its saliva,” [where the second is likened to the first]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "موجب لتقديم المبتدأ.",
     "en": "[This is what] necessitates placing the mubtadaʾ first."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر أنه مثال للمعرفتين.",
     "en": "Apparently it is an example of the two definite [terms]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: لو أريد به التساوي في التعريف والتخصيص كان غنى عن قوله: «أو كانا معرفتين»، لكنه لم يكتف به لذهاب الوهم إلى التساوي في درجة التعريف.",
     "en": "It has been said: if equality in definiteness and specification were meant by it, it would have dispensed with his words “or the two are definite”; but he did not content himself with it, because the mind would go to equality in the degree of definiteness."},
    {"type": "pair",
     "ar": "وفيه أن مثل هذا الوهم غير مهروب عنه لثبوته في التساوي في التخصيص، فالأولى أن يقال: لم يكتف به لفوات التفصيل.",
     "en": "Against this: such a supposition is not avoided [by his wording], since it arises equally with equality in specification. It is better, then, to say: he did not content himself with it because the detailed breakdown would have been lost."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فالمراد التساوي في صحة وقوعه مبتدأ.",
     "en": "So what is meant is equality in the validity of its occurring as a mubtadaʾ."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "مع رعاية الأصل.",
     "en": "Together with observing the basic rule (al-aṣl)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: صورة. فخرج بقوله: «له» «قام أبوه» في «زيد قام أبوه»، وبقوله: «صورة» خرج «الزيدان قاما»؛ لأن الخبر ليس فعلا صورة، كذا قيل.",
     "en": "That is: in form. By his words “belonging to it,” “qāma abūhu” in “Zaydun qāma abūhu” is excluded; and by his words “in form,” “al-Zaydāni qāmā” is excluded, because the khabar is not a verb in form—so it has been said."},
    {"type": "pair",
     "ar": "وفيه أن «زيد قام أبوه» ليس الخبر فيه فعلا صورة، فلا حاجة لإخراجه إلى قيد له.",
     "en": "Against this: in “Zaydun qāma abūhu” the khabar is not a verb in form, so there is no need of a qualification to exclude it."},
    {"type": "pair",
     "ar": "فمعنى قوله: «أو كان الخبر فعلا له»: أو كان الخبر مشتملا على فعل له.",
     "en": "So the meaning of his words “or the khabar is a verb belonging to it” is: or the khabar contains a verb belonging to it."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "ليس الجزاء مقيدا بقوله: «في هذه الصور»، وإلا لكان القيد لغوا لإغناء الشرط عنه،",
     "en": "The apodosis (jazāʾ) is not restricted by his words “in these cases”; otherwise the restriction would be redundant, since the conditional clause renders it unnecessary;"},
    {"type": "pair",
     "ar": "فينبغي أن يحمل على أنه أشار إلي أن الجزاء جزاء لشروط متعددة.",  # «إلي» as printed
     "en": "so it should be taken to mean that he indicated that the apodosis is the apodosis of several conditions."},
]
