# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 333 (printed ٣٣٢)."""

PAGE_NUMBER = 333
PRINTED_PAGE = "٣٣٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وحسن أيضا «قاعدة غلمانه»؛» at the foot of PDF p. 332.
    {"type": "matn",
     "ar": "لأن الفاعل مؤنث غير حقيقي كما حسن «تقعد غلمانه».",
     "en": "…because the agent is non-genuinely feminine, just as “taqʿudu ghilmānuhu” is good."},
    {"type": "matn",
     "ar": "(وضعف) «قام رجل» («قاعدون غلمانه»)؛ لأنه بمنزلة «يقعدون غلمانه»، وإلحاق علامتي المثنى والمجموع في الفعل المسند إلى ظاهرهما ضعيف.",
     "en": "(And “qāma rajulun qāʿidūna ghilmānuhu” is weak), because it is equivalent to “yaqʿudūna ghilmānuhu,” and attaching the signs of the dual and the plural to a verb predicated of an overt dual or plural is weak."},
    {"type": "matn",
     "ar": "(ويجوز) من غير حسن ولا ضعف («قعود غلمانه») وإن كان «قعود» جمعا أيضا كـ«قاعدون»؛",
     "en": "(And “quʿūdun ghilmānuhu” is permissible), being neither good nor weak, even though “quʿūd” is also a plural, like “qāʿidūna”;"},
    {"type": "matn",
     "ar": "لأنك إذا كسرت الاسم المشابه للفعل خرج لفظا عن موازنة الفعل ومناسبته؛ لأن الفعل لا يكسر،",
     "en": "for when you give a broken plural (taksīr) to a noun that resembles the verb, it departs in its wording from the verb’s pattern and from correspondence with it, since the verb is not given a broken plural;"},
    {"type": "matn",
     "ar": "فلم يكن «قعود غلمانه» مثل: «يقعدون غلمانه» الذي اجتمع فيه فاعلان في الظاهر،",
     "en": "so “quʿūdun ghilmānuhu” is not like “yaqʿudūna ghilmānuhu,” in which two agents are combined on the face of it,"},
    {"type": "matn",
     "ar": "إلا أن يخرج[[١]] الواو من الاسمية إلى الحرفية، أو يجعل المظهر بدلا من المضمر، أو يجعل الفعل خبرا مقدما على المبتدأ[[٢]].",
     "en": "unless the wāw is taken out of being a noun into being a particle, or the overt noun is made a substitute for the pronoun, or the verb is made a predicate placed before the subject (mubtadaʾ)."},
    {"type": "matn",
     "ar": "(والمضمر لا يوصف)؛ لأن ضمير المتكلم والمخاطب أعرف المعارف وأوضحها، فلا حاجة لهما إلى التوضيح[[٣]]،",
     "en": "(The pronoun (al-muḍmar) is not qualified), because the pronoun of the speaker and of the addressee are the most definite and clearest of definite nouns, so they have no need of clarification (tawḍīḥ);"},
    {"type": "matn",
     "ar": "وحمل عليهما ضمير الغائب[[٤]]، وعلى الوصف الموضح الوصف المادح والذام وغيرهما طردا للباب",
     "en": "the pronoun of the absent [third person] was assimilated to them, and the praising and blaming description and others were assimilated to the clarifying description, to keep the rule uniform (ṭardan li-l-bāb);"},
    {"type": "matn",
     "ar": "(ولا يوصف به)؛ لأنه ليس في المضمر معنى الوصفية[[٥]] -وهو الدلالة على قيام معنى بالذات- لأنه يدل على",
     "en": "(nor is [anything] qualified by it), because there is in the pronoun no sense of being descriptive—namely signifying that a meaning subsists in an essence—since it signifies…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأولى ترك \"في الظاهر\" ليتصل الاستثناء بلا كلفة ولئلا يتجه أن جعل الاسم الظاهر بعد الضمير بدلا ليس خلاف الظاهر حتى يكون الظاهر اجتماع فاعلين.",
     "en": "It would be better to omit “on the face of it,” so that the exception connects without strain, and so that it cannot be objected that making the overt noun after the pronoun a substitute is not contrary to the apparent sense, such that the apparent sense would be the combination of two agents."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى أو يجعل الجملة،",
     "en": "It would be better [to say]: “or the sentence is made [a predicate placed first].”"},
    {"type": "pair",
     "ar": "ووجهه ما ذكره العلامة التفتازاني في المطول في أواخر أحوال المسند أنه كثيرا ما يطلق الفعل على الفعل مع ضميره المتصل.",
     "en": "Its justification is what al-ʿAllāma al-Taftāzānī mentioned in al-Muṭawwal, towards the end of [the chapter on] the states of the predicate: that “verb” is often applied to the verb together with its attached pronoun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أن أعرف المعارف الذي فوق الجميع ضمير المتكلم الواحد، ومن البين أن ضمير المتكلم مع الغير، والمخاطب ليسا في مرتبته،",
     "en": "Against this: the most definite of definite nouns, above all the rest, is the pronoun of the single speaker; and it is evident that the pronoun of the speaker with others and that of the addressee are not of its rank."},
    # REVIEW: «عدم حاجته المتكلم» is printed thus (pronoun suffix followed by a definite noun); transcribed as printed.
    {"type": "pair",
     "ar": "فلو سلم عدم حاجته إلى التوضيح ليرتقي في الوضوح، فلا نسلم عدم حاجته المتكلم مع الغير والمخاطب ليبلغا مرتبة المتكلم الواحد،",
     "en": "Even if it is granted that it has no need of clarification to rise in clarity, we do not grant that the speaker with others and the addressee have no need of it in order to reach the rank of the single speaker."},
    {"type": "pair",
     "ar": "فالأولى أن يقال: لا حاجة للواحد المتكلم إلى التوضيح، وحمل عليه باقي الضمائر.",
     "en": "It would therefore be better to say: the single speaker has no need of clarification, and the remaining pronouns were assimilated to it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وأجاز الكسائي وصفه متمسكا بقوله تعالى: ﴿لا إله إلا هو العزيز الحكيم﴾ (سورة آل عمران: ٦)،",
     "en": "Al-Kisāʾī permitted qualifying it, holding to the words of the Exalted “There is no god but He, the Mighty, the Wise” (Qurʾān, Sūrat Āl ʿImrān 3:6);"},
    {"type": "pair",
     "ar": "وحمل الجمهور مثله على البدل.",
     "en": "the majority took such cases as substitution (badal)."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: هو من أسماء الله تعالى فهو فيه تعالى اسم ظاهر كما لو جعل الضمير علما، فتأمل.",
     "en": "It may be said: “huwa” is one of the names of Allah the Exalted, so in Him, the Exalted, it is an overt noun, as if the pronoun had been made a proper name. Consider this."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: print reads «الاستعال» (for «الاستعمال», usage); transcribed as printed.
    {"type": "pair",
     "ar": "بحسب الاستعال وإن دل على معنى التكلم والخطاب والغيبة.",
     "en": "With respect to usage, even though it signifies the meaning of first, second or third person."},
    {"type": "pair",
     "ar": "وفيه أن الضمير الراجع إلى اسم الفاعل أو المفعول دال على معنى الوصفية كمرجعه.",
     "en": "Against this: a pronoun referring to an active or passive participle signifies the sense of being descriptive, as does its referent."},
    {"type": "pair",
     "ar": "ويمكن أن يدفع بأن ذلك المعنى إذا كان في قالب الضمير لا يقصد به التوصيف.",
     "en": "This can be answered: when that meaning is in the mould of a pronoun, qualification is not intended by it."},
    {"type": "pair",
     "ar": "والأولى أن يقال في التعليل: إن الموصوف يجب أن يكون أعرف أو مساويا، والضمير أعرف المعارف، فلا يصح الوصف به،",
     "en": "It would be better to say by way of explanation: the qualified must be more definite or equal, and the pronoun is the most definite of definite nouns, so description by it is not sound."},
    {"type": "pair",
     "ar": "فقوله: والموصوف أخص أو مساو إشارة إلى هذا التعليل.",
     "en": "His words “the qualified is more specific or equal” point to this explanation."},
    {"type": "pair",
     "ar": "ولهذا قرنه به، أو اكتفى به، فوقع الدليل موقع المدلول، كما في نسخة الشيخ الرضي.",
     "en": "For this reason he joined it to it, or contented himself with it, so that the proof took the place of what it proves, as in Shaykh al-Raḍī’s copy."},
]
