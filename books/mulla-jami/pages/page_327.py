# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 327 (printed ٣٢٦)."""

PAGE_NUMBER = 327
PRINTED_PAGE = "٣٢٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… يدل بهيئة تركيبية مع متبوعه على» at the foot of PDF p. 326 (mid-sentence).
    {"type": "matn",
     "ar": "حصول معنى في متبوعه[[١]] (مطلقا) أي: دلالة مطلقة[[٢]] غير مقيدة بخصوصية مادة من المواد، احتراز عن سائر التوابع،",
     "en": "…the presence of a meaning in what it follows, (absolutely), that is, an absolute indication not restricted to the particularity of any given material; this excludes the other appositives."},
    {"type": "matn",
     "ar": "ولا يرد عليه البدل في مثل قولك: «أعجبني زيد علمه»، والمعطوف في مثل قولك: «أعجبني زيد وعلمه»، ولا التأكيد في مثل قولك: «جاءني القوم كلهم» لدلالة «كلهم» على معنى الشمول في «القوم»،",
     "en": "No objection is raised against it by the substitute (badal) in such as “Zayd, his learning, pleased me,” by the conjoined noun in such as “Zayd and his learning pleased me,” or by corroboration (taʾkīd) in such as “The people came to me, all of them,” on the ground that “all of them” indicates the meaning of inclusiveness in “the people”;"},
    {"type": "matn",
     "ar": "فإن دلالة التوابع في هذه الأمثلة على حصول معنى في المتبوع إنما هي لخصوص موادها[[٣]]،",
     "en": "for the indication by the appositives in these examples of the presence of a meaning in what is followed is due only to the particularity of their material."},
    {"type": "matn",
     "ar": "فلو جردت عن هذه المواد كما يقال: «أعجبني زيد غلامه» أو «أعجبني زيد وغلامه» أو «جاءني زيد نفسه» لا تجد لها دلالة على معنى في متبوعاتها،",
     "en": "Were they stripped of this material, as when one says “Zayd, his slave, pleased me,” or “Zayd and his slave pleased me,” or “Zayd himself came to me,” you would find in them no indication of a meaning in what they follow;"},
    {"type": "matn",
     "ar": "بخلاف الصفة، فإن الهيئة التركيبية بين الصفة والموصوف تدل على حصول معنى في متبوعها في أي مادة كانت.",
     "en": "unlike the adjective, for the compositional form between adjective and qualified noun indicates the presence of a meaning in what it follows, whatever the material."},
    {"type": "matn",
     "ar": "(وفائدته[[٤]]) أي: فائدة النعت غالبا (تخصيص) في النكرة كـ«رجل عالم» (أو توضيح) في المعرفة كـ«زيد الظريف».",
     "en": "(Its purpose), that is, the purpose of the attribute for the most part, (is specification, takhṣīṣ) with an indefinite noun, as “a learned man,” (or clarification, tawḍīḥ) with a definite noun, as “Zayd the witty.”"},
    {"type": "matn",
     "ar": "(وقد يكون لمجرد الثناء[[٥]]) من غير قصد تخصيص وتوضيح نحو: «بسم الله",
     "en": "(It may be for mere praise), without intending specification or clarification, as in “In the name of Allah…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يذهب عليك أن «أعجبني زيد وعلمه»، و«أعجبني زيد علمه»، و«جاءني القوم كلهم» خرجت بهذا القيد عن التعريف؛",
     "en": "Let it not escape you that “Zayd and his learning pleased me,” “Zayd, his learning, pleased me,” and “The people came to me, all of them” are excluded from the definition by this qualification;"},
    {"type": "pair",
     "ar": "لأن دلالة علمه على حصول صفة في «زيد» ليست بهيئة تركيبية في «زيد»، بل لإضافته إلى ضميره،",
     "en": "for the indication by “his learning” of the presence of an attribute in “Zayd” is not through a compositional form in “Zayd,” but through its annexation to his pronoun;"},
    {"type": "pair",
     "ar": "وكذا دلالة كلهم على الشمول في القوم ليست بهيئة تركيبية، بل لإضافة الكل إلى ضميره،",
     "en": "likewise the indication by “all of them” of inclusiveness in “the people” is not through a compositional form, but through the annexation of “kull” to their pronoun."},
    {"type": "pair",
     "ar": "فلا فائدة لقوله: مطلقا، ولا يتم ما ذكره في بيان فائدته.",
     "en": "So his word “absolutely” serves no purpose, and what he said in explaining its purpose does not hold."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل مطلقا صفة الدلالة، ولا يساعده العبارة؛ لأنه يجب حينئذ تأنيثه مطلقا",
     "en": "He made “muṭlaqan” an attribute of “the indication,” but the wording does not support him, for it would then have to be in the feminine, “muṭlaqatan,”"},
    {"type": "pair",
     "ar": "إلا أن يقال: لم يعتد بتأنيث المصدر، أو بتأنيث ما لا بد له في الدلالة على معناه من التاء.",
     "en": "unless it is said that no account is taken of the femininity of a verbal noun, or of the femininity of a word that needs the tāʾ to indicate its meaning."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ذلك في «أعجبني القوم كلهم» باطل؛ لأن تركيب التأكيد مع المتبوع يفيد التقرير الشمول،",
     "en": "That is false in “The people pleased me, all of them,” because the construction of corroboration with what it follows conveys the confirmation of inclusiveness;"},
    {"type": "pair",
     "ar": "فلولا دلالته على حصول الشمول في متبوعه لم يتقرر به الشمول الذي يدل عليه المتبوع.",
     "en": "were it not for its indicating the presence of inclusiveness in what it follows, the inclusiveness indicated by what is followed would not be confirmed by it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «أراد الفرق بين النعت،» with no second term of «بين»; transcribed as printed.
    {"type": "pair",
     "ar": "أراد الفرق بين النعت، فإن كلا منهما يدل على معنى في شيء،",
     "en": "He meant [to state] the difference between the attribute [and …], for each of them indicates a meaning in something;"},
    {"type": "pair",
     "ar": "يعني: ليس الغرض من الوصف الإعلام بحصول المعنى، بل تخصيص المتبوع إلى غير ذلك.",
     "en": "he means: the purpose of description is not to inform of the presence of the meaning, but the specification of what is followed, and so on."},
    {"type": "pair",
     "ar": "فهذه وظيفة نحوية لا بيانية كما توهم.",
     "en": "This is a grammatical function, not one of rhetoric (bayān), as has been imagined."},
    {"type": "pair",
     "ar": "وإنما يكون وظيفة بيانية لو كان لغرض بيان المزايا التي يجب أن يقصدها المتكلم بالتركيب زائدة على أصل المعنى هذا.",
     "en": "It would be a rhetorical function only if it served to set out the merits that the speaker must intend by the construction over and above the basic meaning. So much for this."},
    {"type": "pair",
     "ar": "والفرق بين التخصيص والتوضيح مجرد اصطلاح نحوي، فإن الأول تقليل الاشتراك في النكرات، والثاني رفع الاحتمال في المعارف،",
     "en": "The difference between specification and clarification is a mere grammatical convention: the first is reducing shared reference in indefinites, the second is removing ambiguity in definites."},
    {"type": "pair",
     "ar": "وكونه غالبا للتخصيص، أو التوضيح يستفاد من تقييد ما يعادلهما بالقلة كما يستفاد من حروف التقليل.",
     "en": "That it is for the most part for specification or clarification is understood from restricting what stands opposite them to rarity, as is understood from the particles of paucity (ḥurūf al-taqlīl)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وقد يكون للتعميم، نحو: كان ذلك في يوم من الأيام.",
     "en": "It may be for generalization, as in “That was on one day of the days.”"},
    {"type": "pair",
     "ar": "وقد يكون للترحم نحو: أنا زيد الفقير، وقد يكون لكشف الماهية نحو: الجسم الطويل العريض العميق.",
     "en": "It may be for eliciting compassion, as in “I am Zayd the poor,” and it may be for disclosing the quiddity (kashf al-māhiyya), as in “body, long, broad, deep.”"},
    {"type": "pair",
     "ar": "والفرق بين الصفة الكاشفة والصفة المؤكدة: بأن الأولى موضحة مفسرة، والثانية مقررة. والفرق بين بين الإيضاح والتقرير.",
     "en": "The difference between the disclosing adjective and the corroborating adjective is that the first clarifies and explains, while the second confirms; and the difference between clarification and confirmation is plain."},
    {"type": "pair",
     "ar": "وقيل: الفرق بينهما أن المؤكدة تؤكد بعض مفهوم الموصوف كأمس الدابر ونفخة واحدة. والكاشفة تكشف عن",
     "en": "It has been said: the difference between them is that the corroborating adjective corroborates part of the concept of the qualified noun, as in “yesterday, the bygone” and “a single blast,” while the disclosing adjective discloses…"},
]
