# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 263 (printed ٢٦٢)."""

PAGE_NUMBER = 263
PRINTED_PAGE = "٢٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «سواء كانت (ظاهرة) في اللفظ نحو: ...» from the foot of PDF p. 262.
    {"type": "matn",
     "ar": "(أو مقدرة) منوية نحو قوله تعالى: ﴿أو جاءوكم حصرت صدورهم﴾[[١]]، أي: قد حصرت صدورهم.",
     "en": "…(or understood), intended [though unexpressed], as in His words, the Exalted: “or [who] come to you, their breasts constrained,” that is: “their breasts having [qad] become constrained.”"},
    {"type": "matn",
     "ar": "وهذا بخلاف مذهب سيبويه والمبرد، فإنهما لا يجوزان حذف «قد»،",
     "en": "This is contrary to the doctrine of Sībawayh and al-Mubarrad, for they do not permit the elision of “qad.”"},
    {"type": "matn",
     "ar": "فسيبويه يؤول قوله تعالى: ﴿حصرت صدورهم﴾[[٢]] بـ«قوما حصرت صدورهم»، فتكون جملة «حصرت» صفة موصوف محذوف هو الحال،",
     "en": "Sībawayh construes His words, the Exalted, “their breasts constrained” as “a people whose breasts are constrained”; so the clause “ḥaṣirat” is an adjective of an elided qualified noun, which is the ḥāl;"},
    {"type": "matn",
     "ar": "والمبرد يجعله جملة دعائية،",
     "en": "while al-Mubarrad takes it as a clause of supplication (duʿāʾiyya)."},
    {"type": "matn",
     "ar": "وإنما لم يشترط ذلك في المنفي، لاستمرار النفي بلا قاطع، فيشتمل زمان الفعل.",
     "en": "This is not required in the negated [perfect] only because the negation continues without interruption, and so it encompasses the time of the action."},
    {"type": "matn",
     "ar": "(ويجوز حذف العامل[[٣]]) في الحال لقيام قرينة حالية",
     "en": "(The governor may be elided) in the ḥāl when a contextual indication from the situation (qarīna ḥāliyya) is present,"},
    {"type": "matn",
     "ar": "(كقولك للمسافر) أي: الشارع في السفر أو المتهيئ له («راشدا مهديا») أي: سر راشدا مهديا، بقرينة حال المخاطب،",
     "en": "(as in your saying to the traveller), that is, one setting out on a journey or preparing for it, (“rightly guided, well directed”), that is, “Go, rightly guided, well directed,” by indication of the addressee’s situation."},
    {"type": "matn",
     "ar": "وقوله: «مهديا» إما صفة لـ«راشدا»، أو حال بعد حال،",
     "en": "His word “mahdiyyan” is either an adjective of “rāshidan” or a ḥāl following a ḥāl;"},
    {"type": "matn",
     "ar": "أو مقالية كقولك: «راكبا» لمن يقول: «كيف جئت؟» أي: جئت راكبا بقرينة السؤال،",
     "en": "or [the indication is] verbal (maqāliyya), as in your saying “riding” to one who says “How did you come?”, that is, “I came riding,” by indication of the question."},
    {"type": "matn",
     "ar": "ومنه قوله تعالى: ﴿أيحسب الإنسان ألن نجمع عظامه، بلى قادرين﴾[[٤]]، أي: بلى نجمعها قادرين.",
     "en": "Of this kind are His words, the Exalted: “Does man think that We will not gather his bones? Yes indeed, [We are] able,” that is: “Yes, We will gather them, being able.”"},
    {"type": "matn",
     "ar": "(ويجب) حذف العامل (في) بعض الأحوال (المؤكدة[[٥]])",
     "en": "(And it is obligatory) to elide the governor (in) certain (corroborative) ḥāls."},
    {"type": "matn",
     "ar": "وهي أي: الحال المؤكدة مطلقا هي التي لا تنتقل من صاحبها ما دام موجودا غالبا بخلاف المنتقلة،",
     "en": "It, that is, the corroborative ḥāl in general, is one that does not, as a rule, leave its owner as long as it exists, unlike the transient [ḥāl];"},
    {"type": "matn",
     "ar": "والمنتقلة قيد للعامل، بخلاف المؤكدة[[٦]]",
     "en": "and the transient ḥāl is a restriction on the governor, unlike the corroborative,"},
    {"type": "matn",
     "ar": "(مثل: «زيد أبوك عطوفا») فإن العطوفية لا تنتقل عن الأب في غالب الأمر",
     "en": "(as in: “Zayd is your father, compassionate”), for compassion does not, as a rule, leave a father;"},
    {"type": "matn",
     "ar": "(أي: أحقه) بفتح الهمزة أو ضمها من «حققت الأمر» بمعنى: تحققته وصرت منه على يقين،",
     "en": "(that is, “I affirm him [aḥuqquhu]”), with a fatḥa or ḍamma on the hamza, from “ḥaqaqtu al-amr,” meaning “I ascertained it and became certain of it,”"},
    {"type": "matn",
     "ar": "أو من: «أحققت الأمر» بهذا المعنى بعينه أو بمعنى",
     "en": "or from “aḥqaqtu al-amr” in exactly this sense, or in the sense of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة النساء: ٩٠.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:90."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النساء: ٩٠.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:90."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وقد يجب قياسا في مواضع: منها: ما إذا بين الحال ازدياد ثمن أو غيره مقرونة بالفاء أو ثم،",
     "en": "It is sometimes obligatory, as a regular rule, in certain places, among them: where the ḥāl, joined with fa- or thumma, makes clear an increase in price or the like."},
    {"type": "pair",
     "ar": "فتقول في الثمن: بعته بدرهم فصاعدا أو ثم زائدا أي: فذهب الثمن صاعدا، أو ثم ذهب الثمن زائدا آخذا في الازدياد.",
     "en": "So you say of a price: “I sold it for a dirham and upward,” or “and then more,” that is, “and the price went upward,” or “then the price went on increasing, taking to increase.”"},
    {"type": "pair",
     "ar": "وتقول في غير الثمن قرأت كل يوم جزءا من القرآن فصاعدا، أو ثم زائدا أي: فذهبت القراءة كل يوم في الزيادة والصعود.",
     "en": "And of other than price you say: “I read a part of the Qurʾān each day and upward,” or “and then more,” that is, “the reading went on each day increasing and rising.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة القيامة: ٣-٤.",
     "en": "Qurʾān, Sūrat al-Qiyāma 75:3–4."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وكذا في حال تبين ازدياد ثمن، أو غيره مما دخله الفاء أو ثم نحو: بعته بدرهم فصاعدا، وقرأت جزءا من القرآن فصاعدا أي: فذهب القراءة في الصعود.",
     "en": "Likewise in a ḥāl that makes clear an increase in price or the like, which fa- or thumma has entered, as in “I sold it for a dirham and upward” and “I read a part of the Qurʾān and upward,” that is, “the reading went upward.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإنها ليست قيدا مخصصا للعامل، فالقول بأن الحال مطلقا قيد للعامل غير صحيح إلا أن يراد أنها قيد له بحسب العبارة والتصور.",
     "en": "For it is not a restriction that specifies the governor; so the claim that the ḥāl in general is a restriction on the governor is not correct, unless what is meant is that it restricts it in expression and conception."},
]
