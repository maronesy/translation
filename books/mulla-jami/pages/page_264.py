# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 264 (printed ٢٦٣)."""

PAGE_NUMBER = 264
PRINTED_PAGE = "٢٦٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أو من: «أحققت الأمر» بهذا المعنى بعينه أو بمعنى» from the foot of PDF p. 263.
    {"type": "matn",
     "ar": "أثبته، أي: تحققت أبوته[[١]] لك وصرت منها على يقين، أو أثبتها كذلك عطوفا،",
     "en": "…“I established it”; that is: his fatherhood has been verified for you and you have become certain of it, or: establish it thus, as affectionate."},
    {"type": "matn",
     "ar": "وقال صاحب المفتاح: أحق التقديرات عندي أن يقدر: يحني عطوفا.",
     "en": "The author of al-Miftāḥ said: the most correct of the supplied readings in my view is that one supply “he bends [over you] affectionately.”"},
    {"type": "matn",
     "ar": "(وشرطها) أي: شرط وجوب حذف عاملها[[٢]] (أن تكون مقررة) أي: مؤكدة (لمضمون جملة)",
     "en": "(Its condition), that is, the condition for the obligatory elision of its governor, (is that it confirm), that is, corroborate, (the content of a sentence)."},
    {"type": "matn",
     "ar": "احترز به عما يؤكد بعض أجزائها كالعامل في قوله تعالى: ﴿وأرسلناك للناس رسولا﴾[[٣]]، فإنه لا يجب حذفه",
     "en": "By this he excludes that which corroborates one of its parts, such as the governor in His words, the Exalted: “And We have sent you to mankind as a messenger”; for its elision is not obligatory."},
    {"type": "matn",
     "ar": "(اسمية) احترز به عما إذا كانت فعلية، فإنه لا يجب حذف عاملها،",
     "en": "([A] nominal [sentence]): by this he excludes the case where it is verbal, for the elision of its governor is then not obligatory,"},
    {"type": "matn",
     "ar": "كما قال صاحب الكشاف في قوله تعالى: ﴿قائما بالقسط﴾[[٤]] إنه حال مؤكدة من فاعل «شهد»",
     "en": "as the author of al-Kashshāf said of His words, the Exalted: “maintaining [it] in justice,” that it is a corroborative circumstantial qualifier (ḥāl muʾakkida) from the agent of “shahida” (He bore witness)."},
    {"type": "matn",
     "ar": "ولا بد ههنا من قيد آخر، وهو أن يكون عقد تلك الاسمية من اسمين لا يصلحان للعمل فيها،",
     "en": "A further restriction is needed here: that the nominal sentence be composed of two nouns neither of which is fit to govern it;"},
    {"type": "matn",
     "ar": "وإلا لكان عاملها مذكورا، فكيف يكون حذفه واجبا، نحو: «الله شاهد قائما بالقسط».",
     "en": "otherwise its governor would be mentioned, so how could its elision be obligatory? As in “Allah is witnessing, maintaining [it] in justice.”"},

    {"type": "section", "ar": "[التمييز]",
     "en": "The Specifying Noun (al-Tamyīz)"},

    {"type": "matn",
     "ar": "(التمييز[[٥]]: ما) أي: الاسم الذي (يرفع الإبهام).",
     "en": "(The specifying noun (tamyīz) is that which), that is, the noun which, (removes vagueness)."},
    {"type": "matn",
     "ar": "واحترز به عن البدل، فإن المبدل منه حكم التنحية، فهو ليس يرفع الإبهام عن شيء، بل هو ترك مبهم وإيراد معين.",
     "en": "By this he excludes the substitute (badal); for the replaced term (mubdal minhu) is treated as set aside, so [the badal] does not remove vagueness from anything; rather it is the abandoning of something vague and the bringing in of something determinate."},
    {"type": "matn",
     "ar": "(المستقر) أي: الثابت الراسخ في المعنى الموضوع له، من حيث إنه موضوع له[[٦]].",
     "en": "(Settled), that is, fixed and firmly lodged in the meaning for which it was coined, inasmuch as it was coined for it."},
    {"type": "matn",
     "ar": "فإن المستقر وإن كان بحسب اللغة هو الثابت مطلقا، لكن المطلق منصرف إلى",
     "en": "For although “settled” (mustaqirr) in the lexical sense is the fixed without qualification, the unqualified term is directed to…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "دفع لما ذكره المحقق الرضي من أنه لا معنى لقولك: تيقنت الأب في حال كونه عطوفا،",
     "en": "[This is] a rebuttal of what the meticulous scholar al-Raḍī mentioned, namely that there is no sense in your saying “I became certain of the father while he is affectionate.”"},
    {"type": "pair",
     "ar": "نعم يصح أن يكون المعنى أعلمه عطوفا، لكن عطوفا حينئذ مفعول ثان لا حال.",
     "en": "Admittedly, the meaning could correctly be “I know him [to be] affectionate,” but “affectionate” would then be a second object, not a ḥāl."},
    {"type": "pair",
     "ar": "ووجه الدفع أن حقه في تقدير أحق أبوته بحذف المضاف لظهور المقصود وإقامة المضاف إليه مقامه، وهكذا أثبته.",
     "en": "The point of the rebuttal is that its proper construal is “I verify his fatherhood,” with the first term of the genitive construction (muḍāf) elided because the intended sense is evident, and the second term (muḍāf ilayhi) put in its place; and likewise “I established it.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أو شرطها في وجوب حذف عاملها.",
     "en": "Or: its condition with respect to the obligatory elision of its governor."},
    {"type": "pair",
     "ar": "إنما قدرت هذه الأمور الثلاثة؛ لأن الحق أن الحال المؤكدة قد تكون مؤكدة لجملة فعلية،",
     "en": "These three things have been supplied only because the truth is that a corroborative ḥāl may corroborate a verbal sentence,"},
    {"type": "pair",
     "ar": "كقوله تعالى: ﴿ولا تعثوا في الأرض مفسدين﴾ (الشعراء:١٨٣) أي: لا تفسدوا.",
     "en": "as in His words, the Exalted: “And do not commit abuse on earth, spreading corruption” (Qurʾān, Sūrat al-Shuʿarāʾ 26:183), that is: do not spread corruption."},
    {"type": "pair",
     "ar": "ومن خصص المؤكدة بالجملة الاسمية يؤول أمثاله بالمصادر، فيجعل قوله تعالى: «مفسدين» بمعنى الإفساد.",
     "en": "Whoever restricts the corroborative [ḥāl] to the nominal sentence interprets such examples as verbal nouns (maṣādir), taking His words, the Exalted, “mufsidīn” to mean “corruption” (ifsād)."},
    {"type": "pair",
     "ar": "وكثيرا ما يجيء صيغة الصفة مقام المصدر.",
     "en": "The adjectival form frequently comes in place of the maṣdar."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة النساء: ٧٩.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:79."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة آل عمران: ١٨.",
     "en": "Qurʾān, Sūrat Āl ʿImrān 3:18."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ويقال له: التبيين والتفسير والمميز بكسر الياء.",
     "en": "It is also called tabyīn (clarification), tafsīr (explanation) and mumayyiz, with kasra on the yāʾ."},
    {"type": "pair",
     "ar": "قيل: وقد يقال بفتحها؛ لأن المتكلم يميزه من بين الأجناس، ويرفع الإبهام.",
     "en": "It has been said: it is also called [mumayyaz] with fatḥa on it, because the speaker distinguishes it from among the genera and removes the vagueness."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لعل الوضع شامل للوضع النوعي المجازي؛ لأن أسماء العدد والوزن والكيل إذا أريد بها المعاني الحقيقية، وهي العدد والكيل والوزن لا تستدعي تمييزا.",
     "en": "Perhaps “coinage” (waḍʿ) includes the figurative generic coinage (al-waḍʿ al-nawʿī al-majāzī); for nouns of number, weight and measure, when their literal meanings are intended, namely number, measure and weight, do not call for a tamyīz."},
    {"type": "pair",
     "ar": "وإنما تستدعيه إذا أريد بها المعدود والمكيل والموزون.",
     "en": "They call for it only when what is meant by them is the thing counted, measured or weighed."},
]
