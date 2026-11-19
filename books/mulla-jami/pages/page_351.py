# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 351 (printed ٣٥٠)."""

PAGE_NUMBER = 351
PRINTED_PAGE = "٣٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وكذا في «سلب زيد ثوبه»،» at the foot of PDF p. 350.
    {"type": "matn",
     "ar": "بخلاف «ضربت زيدا حماره[[١]]، وضربت زيدا غلامه»؛ لأن نسبة الضرب إلى «زيد» تامة، ولا يلزم في صحتها اعتبار غير «زيد»، فيكون من باب بدل الغلط",
     "en": "…unlike “ḍarabtu Zaydan ḥimārahu” (I struck Zayd, his donkey) and “ḍarabtu Zaydan ghulāmahu” (I struck Zayd, his slave), because the attribution of striking to Zayd is complete, and its soundness does not require considering anything other than Zayd; so it belongs to the class of the substitute of error."},
    {"type": "matn",
     "ar": "(بغيرهما[[٢]]) أي: تكون تلك الملابسة بغير كون البدل كل المبدل منه أو جزؤه،",
     "en": "(Other than these two), that is, that connection consists in something other than the substitute’s being the whole of what is substituted for or a part of it."},
    {"type": "matn",
     "ar": "فيدخل فيه[[٣]] ما إذا كان المبدل منه جزءا من البدل ويكون إبداله منه بناء على هذه الملابسة نحو: «نظرت إلى القمر فلكه[[٤]]»،",
     "en": "So there falls under it the case in which what is substituted for is a part of the substitute, and the substitution is made on the basis of this connection, as in “naẓartu ilā al-qamari falakihi” (I looked at the moon, its sphere)."},
    {"type": "matn",
     "ar": "والمناقشة بأن «القمر» ليس جزءا من فلكه، بل هو مركوز فيه مناقشة في المثال،",
     "en": "The objection that the moon is not a part of its sphere, but is set fast in it, is an objection to the example."},
    {"type": "matn",
     "ar": "ويمكن أن يورد لمثاله مثل: «رأيت درجة الأسد برجه»، فإنه لا مجال لهذه المناقشة فيه، فإن البرج عبارة عن مجموع الدرجات،",
     "en": "One may bring as its example something like “raʾaytu darajata al-asadi burjahu” (I saw the degree of Leo, its sign), for there is no room for this objection in it, since the zodiacal sign (burj) denotes the totality of the degrees."},
    {"type": "matn",
     "ar": "وإنما لم يجعل هذا البدل قسما خامسا ولم يسم ببدل الكل عن البعض لقلته وندرته بل قيل: لعدم وقوعه في كلام العرب فإن هذه الأمثلة مصنوعة.",
     "en": "This substitute was not made a fifth category, nor named “the substitute of the whole for the part”, only because it is rare and uncommon—indeed it has been said: because it does not occur in the speech of the Arabs, for these examples are contrived."},
    {"type": "matn",
     "ar": "(والرابع) أي: بدل الغلط (أن تقصد) أي: يكون بأن تقصد أنت (إليه) أي: إلى البدل من غير اعتبار ملابسة بينهما (بعد أن غلطت بغيره[[٥]]) أي: بغير البدل، وهو المبدل منه.",
     "en": "(And the fourth), that is, the substitute of error, (is that you intend), that is, it comes about by your intending, (it), that is, the substitute, without considering any connection between the two, (after you erred with something else), that is, with something other than the substitute, namely what is substituted for."},
    {"type": "matn",
     "ar": "(ويكونان) أي: البدل والمبدل منه (معرفتين) نحو: «ضرب زيد أخوك» (ونكرتين) نحو: «جاء رجل غلام لك»",
     "en": "(They may be), that is, the substitute and what is substituted for, (two definites), as in “ḍaraba Zaydun akhūka” (Zayd, your brother, struck), (and two indefinites), as in “jāʾa rajulun ghulāmun laka” (a man came, a slave of yours),"},
    {"type": "matn",
     "ar": "(ومختلفتين) نحو: ﴿بالناصية ناصية كاذبة﴾[[٦]]، و«جاء رجل غلام زيد».",
     "en": "(and differing), as in “by the forelock, a lying forelock” and “jāʾa rajulun ghulāmu Zaydin” (a man came, Zayd’s slave)."},
    {"type": "matn",
     "ar": "(وإذا كان) البدل[[٧]] (نكرة) مبدلة (من معرفة فالنعت[[٨]]) أي: نعت البدل النكرة",
     "en": "(When) the substitute (is an indefinite) substituted (for a definite, then a qualifying adjective), that is, qualifying the indefinite substitute…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فلا بد من اعتبار ذلك القيد لإخراجه وإخراج ما ذكرناه.",
     "en": "So that restriction must be taken into account, to exclude it and to exclude what we have mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى والأوضح ترك باء الملابسة، والقول بأن بينهما ملابسة غيرهما.",
     "en": "It would have been better and clearer to drop the bāʾ of connection and to say that between them there is a connection other than these two."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: يلزم ثبوت قسم خامس.",
     "en": "That is, [otherwise] a fifth category would have to be posited."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن النسبة إلى المبدل منه لا يوجب النسبة إلى البدل، فكيف يكون مثالا لبدل الاشتمال. وكذا المثال الأخير.",
     "en": "Against this: the attribution to what is substituted for does not entail the attribution to the substitute, so how can it be an example of the substitute of inclusion? The same applies to the last example."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وفيه نظر لأن القصد إلى البدل قبل الغلط، وإنما ذكر خلاف ما قصد بالقصد أو النسيان أو سبق اللسان،",
     "en": "This is open to question, because the intention toward the substitute precedes the error; what was mentioned contrary to what was intended came about by intention, forgetfulness or a slip of the tongue."},
    {"type": "pair",
     "ar": "فكأنه أريد أن يقصد إلى البدل من حيث إنه بدل يعني: أن يقصد إلى الإبدال بعد أن غلطت بغيره، فافهم.",
     "en": "So it is as though what is meant is that one intends the substitute inasmuch as it is a substitute, that is, one intends the act of substitution after you erred with something else. So understand."},
    {"type": "pair",
     "ar": "ولم يقل: بعد أن غلطت بالأول تفننا.",
     "en": "He did not say “after you erred with the first”, for stylistic variation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة العلق: ١٥-١٦.",
     "en": "Qurʾān, Sūrat al-ʿAlaq 96:15–16."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يجوز أن يكون نكرة بالرفع. ومعناه: إذا كان نكرة مبدلة من معرفة.",
     "en": "“Nakira” may be in the nominative; its meaning is then: when there is an indefinite substituted for a definite."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "نقل عن المصنف أنه جعل هذا توجيها لتوصيف بدل الكل.",
     "en": "It is reported of the author that he made this the explanation for qualifying the substitute of the whole."},
    {"type": "pair",
     "ar": "وأما في وجه توصيف بدل البعض والاشتمال فقد قال: إنهما لا بد فيهما من ضمير يرجع إلى المتبوع ليعلم أنه بعضه أو ملابسه",
     "en": "As for the reason for qualifying the substitute of the part and of inclusion, he said: the two must contain a pronoun referring to the antecedent, so that it is known to be a part of it or connected with it;"},
    {"type": "pair",
     "ar": "فلو كان متصلا لكان معرفة، ولو كان مفصولا لكان متصفا به.",
     "en": "if [the pronoun] were attached, [the substitute] would be definite, and if it were separate, [the substitute] would be qualified by it."},
]
