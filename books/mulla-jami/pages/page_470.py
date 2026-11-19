# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 470 (printed ٤٦٩)."""

PAGE_NUMBER = 470
PRINTED_PAGE = "٤٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أن المحذوف» at the foot of PDF p. 469 (mid-sentence).
    {"type": "matn",
     "ar": "هو المضاف إليه، أي: «أكبر كل شيء»، أو إنه «من» مع مجروره، أي: «أكبر من كل شيء».",
     "en": "…is the second term of the annexation, that is, “akbaru kulli shayʾ” (the greatest of all things), or that it is “min” with its object, that is, “akbaru min kulli shayʾ” (greater than everything)."},
    {"type": "matn",
     "ar": "(فإذا أضيف) أي: اسم التفضيل (فله معنيان):",
     "en": "(When it is annexed), that is, the elative, (it has two meanings):"},
    {"type": "matn",
     "ar": "(أحدهما: وهو الأكثر أن يقصد به الزيادة) أي: أحدهما: زيادة الموصوفة المقصود به",
     "en": "(The first, which is the more frequent, is that excess be intended by it), that is, the first is the excess of the qualified thing intended by it"},
    {"type": "matn",
     "ar": "(على من أضيف[[١]] إليه) أي: على ما أضيف اسم التفضيل إليه باعتبار تحققه في ضمن بعضهم[[٢]]، وإلا يلزم تفضيل الشيء على نفسه،",
     "en": "(over those to whom it is annexed), that is, over what the elative is annexed to, considered as realized within some of them; otherwise preferring a thing over itself would follow."},
    {"type": "matn",
     "ar": "وإنما كان هذا الاستعمال أكثر؛ لأن وضع «أفعل» لتفضيل الشيء على غيره[[٣]]، فالأولى ذكر المفضول عليه",
     "en": "This usage is more frequent only because “afʿal” is coined for preferring a thing over another, so it is more fitting to mention the one surpassed."},
    {"type": "matn",
     "ar": "(فيشترط) في استعماله بهذا المعنى (أن يكون) موصوفه بعضا (منهم) داخلا فيهم بحسب مفهوم اللفظ، وإن كان خارجا عنهم بحسب الإرادة؛",
     "en": "(So it is a condition) in using it in this sense (that) its qualified thing (be) a part (of them), included among them according to the concept of the expression, even if it is outside them according to what is meant;"},
    {"type": "matn",
     "ar": "لأن المقصود من استعماله بهذا المعنى تفضيل موصوفه على مشاركيه في هذا المفهوم العام",
     "en": "because the purpose of using it in this sense is to prefer its qualified thing over those who share with it in this general concept,"},
    {"type": "matn",
     "ar": "(مثل: «زيد أفضل الناس») أي: أفضل من مشاركيه في هذا النوع",
     "en": "(as in “Zaydun afḍalu l-nās” (Zayd is the most excellent of people)), that is, more excellent than those who share with him in this species."},
    {"type": "matn",
     "ar": "(فلا يجوز) بهذا المعنى قولك: («يوسف أحسن إخوته» لخروجه عنهم) أي: عن الإخوة (بإضافتهم إليه).",
     "en": "(So it is not permitted), in this sense, to say (“Yūsufu aḥsanu ikhwatihi” (Joseph is the most handsome of his brothers), because he is outside them), that is, the brothers, (by their being annexed to him)."},
    {"type": "matn",
     "ar": "(والثاني: أن يقصد زيادة مطلقة) أي: ثاني معنييه زيادة مقصودة مطلقة غير مقيدة بأن يكون على المضاف إليه وحده[[٤]]",
     "en": "(The second is that absolute excess be intended), that is, the second of its two meanings is an intended excess that is absolute, not restricted to being over the second term of the annexation alone;"},
    {"type": "matn",
     "ar": "(ويضاف) اسم التفضيل إلى ما أضيف إليه (للتوضيح) أي: لتوضيح اسم التفضيل وتخصيصه[[٥]]،",
     "en": "(and it is annexed), the elative, to what it is annexed to, (for clarification), that is, to clarify the elative and particularize it,"},
    {"type": "matn",
     "ar": "كما يضاف سائر الصفات نحو: «مصارع مصر، وحسن القوم» مما لا تفضيل فيه، فلا يشترط كونه بعض المضاف إليه",
     "en": "as other adjectives are annexed, as in “muṣāriʿu Miṣr” (the wrestler of Egypt) and “ḥasanu l-qawm” (the handsome one of the people), in which there is no preference; so it is not a condition that it be part of the second term of the annexation…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 469 (printed ٤٦٨), note ٧ ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "وشبهها.",
     "en": "…and what resembles them."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «فيه إشارة إلا أن الأولى» and «بدل من إلا أنه»; «إلى أن» may be intended at least in the first place. Transcribed as printed.
    {"type": "pair",
     "ar": "فيه إشارة إلا أن الأولى إيراد ما بدل من إلا أنه غلب العقلاء على غيرهم.",
     "en": "In it is an indication that it would have been better to use “mā” instead of “man”, except that he gave rational beings precedence over others."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى في ضمن ما عدا المفضل لئلا يتوهم أنه يصح قيد التفضيل باعتبار أي: بعض كان.",
     "en": "It would be better [to say] “within what is other than the one preferred”, lest it be supposed that the restriction of preference holds with regard to any part whatever."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «غير الفضل عليه»; «المفضل عليه» expected. Transcribed as printed.
    {"type": "pair",
     "ar": "لا يخفى أن هذا الوجه يفيد وجه التزام الإضافة، ولو إلى غير الفضل عليه كما في القسم الثاني من الإضافة.",
     "en": "It is not hidden that this reason yields the reason for the necessity of annexation, even to other than the one surpassed, as in the second kind of annexation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يوهم أن الإطلاق معناه الإطلاق على المضاف إليه، وليس كذلك بل معناه الإطلاق بمعنى الزيادة على جميع من سواه صرح به الرضي",
     "en": "It suggests that absoluteness means absoluteness with respect to the second term of the annexation; but it is not so: it means absoluteness in the sense of excess over all others besides it, as al-Raḍī stated explicitly;"},
    {"type": "pair",
     "ar": "إلا أنه يشبه أن يكون المراد بجميع من سواه الجميع حقيقة أو عرفا مما يتبادر عرفا قصد تفضيله عليه.",
     "en": "except that it seems that what is meant by “all others besides it” is all, really or conventionally, among those over whom it is conventionally understood at once that preference is intended."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "زاد قوله: وتخصيصه؛ لأن الإضافة إذا كانت إلى النكرة للتخصيص،",
     "en": "He added his words “and particularize it” because annexation to an indefinite noun is for particularization (takhṣīṣ)."},
    {"type": "pair",
     "ar": "وفيه أنه لا حاجة إلى ذكره؛ لأن الإضافة للتوضيح يشمل التعريف والتخصيص،",
     "en": "Against this: there is no need to mention it, because annexation for clarification includes definition (taʿrīf) and particularization;"},
    {"type": "pair",
     "ar": "ولا تقابل بين الإضافة للتخصيص، والإضافة للتوضيح، وإنما التقابل بين الإضافة للتعريف والإضافة للتخصيص.",
     "en": "there is no opposition between annexation for particularization and annexation for clarification; the opposition is only between annexation for definition and annexation for particularization."},
    {"type": "pair",
     "ar": "وقوله: نحو قولك: نبينا إلى آخره.",
     "en": "And his words: “as in your saying: ‘Our Prophet…’” to the end."},
    {"type": "pair",
     "ar": "أقول: ونحو: محمد أفضل البشر حيث يراد أنه أفضل جميع المخلوقات من جنس البشر.",
     "en": "I say: and as in “Muḥammad is the most excellent of mankind”, where it is meant that he is the most excellent of all creatures of the human genus."},
]
