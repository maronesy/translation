# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 78 (printed ٧٧)."""

PAGE_NUMBER = 78
PRINTED_PAGE = "٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn + sharḥ) ----------------
    {"type": "matn",
     "ar": "والمجموع في كون معانيها منبئة عن تعدد، ولوجود حرف صالح[[١]] للإعراب في أواخرها سماعا، بخلاف سائر الأسماء المحذوفة الأعجاز كـ«يد ودم»، فإنه لم يسمع فيها[[٢]] من العرب إعادة الحروف المحذوفة[[٣]] عند الإعراب.",
     "en": "and the plural [too] — [the resemblance lies] in that their meanings connote plurality, and in that there exists at their ends a letter fit for [bearing] declension, [as established] by transmission (samāʿ); unlike the rest of the nouns whose final [radicals] are elided, such as yad (hand) and dam (blood), for it has not been heard from the Arabs that the elided letters are restored to them at the time of declension."},
    {"type": "matn",
     "ar": "(المثنى) وما يلحق به، (و) هو (كلا[[٤]]) وكذا (كلتا[[٥]])، ولم يذكره لكونه فرع «كلا»، ... (مضافا) أي: حال كون «كلا» أو «كلتا» مضافا (إلى مضمر).",
     "en": "(al-muthannā, the dual) and what is annexed to it, (and) that is (kilā [both, masc.]) and likewise (kiltā [both, fem.]) — he did not mention it [separately] because it is a branch of kilā — ... (annexed [muḍāfan]), that is, in the state of kilā or kiltā being annexed (to a pronoun [ilā muḍmar])."},
    {"type": "matn",
     "ar": "وإنما قيد بذلك؛ لأن «كلا» باعتبار لفظه مفرد، وباعتبار معناه مثنى،",
     "en": "He restricted it with that [condition] only because kilā, with respect to its wording, is singular, but with respect to its meaning, is dual;"},
    {"type": "matn",
     "ar": "فلفظه يقتضي الإعراب بالحركات، ومعناه يقتضي الإعراب بالحروف، فروعي فيه كلا الاعتبارين[[٦]].",
     "en": "so its wording requires declension by vowels, while its meaning requires declension by letters; thus both considerations were observed in it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فاستكرهوا من كلفة اجتلاب حروف أجنبية، مع أن اللام في أربعة منها كأنها مجلوبة للإعراب فقط؛ لكونها محذوفة قبل نسيا منسيا، فهي إذن كالحركات المجتلبة للإعراب، وكذا الواو في فوك؛ لأنها كانت مبدلة منها الميم في الإفراد، فلم ترد إلى أصلها إلا للإعراب.",
     "en": "So they found it burdensome to fetch in extraneous letters, even though the lām in four of them is, as it were, fetched in for declension only — since it had earlier been elided into utter oblivion — and is therefore like the vowels fetched in for declension; and likewise the wāw in fūk, for it had been replaced by the mīm in the singular [fam], and so it is not restored to its origin except for [the sake of] declension."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الأقرب عندي أن اللام في الأربعة الأول، والعين في الباقيين، في حالة الرفع علم العمدة، والألف والياء في النصب والجر علم الفضلة والمضاف إليه، مع كونهما بدلين من لام الكلمة وعينها، وجعل ما قبلها من الحركات من جنسها للتخفيف.",
     "en": "Al-Shaykh al-Raḍī said: what is closest [to correctness] in my view is that the lām in the first four, and the ʿayn in the rest, in the state of rafʿ is the mark of the principal element (ʿumda); while the alif and the yāʾ in the accusative and the genitive are the mark of the complement (faḍla) and of the muḍāf ilayh — both being substitutes for the lām and the ʿayn of the word — and the vowel preceding them was made of their [own] kind for the sake of lightening."},
    {"type": "pair",
     "ar": "وقال المصنف: إن الواو والألف والياء مبدلة من لام الكلمة في أربعة، ومن عينها في الباقيين؛ لأن دليل الإعراب لا يكون من سنخ الكلمة، فهي بدل ما لم يفده المبدل منه، وهو الإعراب، كالتاء في بنت تفيد التأنيث، ولا يبقى ذو وفوك على حرف لقيام البدل مقام المبدل منه. واعترض عليه بألا محذور في جعل الإعراب من سنخ الكلمة لغرض التخفيف كما في المثنى والمجموع، وله أن يقول: إن علامتي التثنية والجمع ليستا من حروف المباني، بل من حروف المعاني.",
     "en": "The author said: the wāw, the alif, and the yāʾ are substitutes for the lām of the word in four [of them], and for its ʿayn in the remaining ones; because the marker of declension cannot be of the essential fabric (sinkh) of the word — for it is a substitute conveying what that which it replaced did not convey, namely declension, just as the tāʾ in bint conveys the feminine; and neither dhū nor fūk is left standing on [only] one letter, since the substitute stands in the place of that which it replaced. It was objected against him that there is no impediment to making the declension [a marker drawn] from the essential fabric of the word for the purpose of lightening, as in the dual and the plural; and he may answer: the two markers of the dual and the plural are not among the letters of structure (ḥurūf al-mabānī), but among the letters of meaning (ḥurūf al-maʿānī)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في الأسماء المحذوفة الأواخر غير الأسماء الستة.",
     "en": "That is: among the nouns whose ends are elided, other than the six nouns."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من الأواخر.",
     "en": "[Namely,] those of the final [letters]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وهو ليس بمثنى؛ لأنه لم يثبت «كل» في المفرد، ولجواز رجوع ضمير الواحد إليه كقولك: كلا الرجلين جاء، قال الله تعالى: ﴿كلتا الجنتين آتت أكلها﴾ (سورة الكهف: ٣٣)، وللزوم الألف في الأحوال الثلاث حال إضافته إلى المظهر، ولجواز إمالته، فإن المثنى لا يمال.",
     "en": "It [kilā] is not [truly] a dual, because “kull” is not established as its singular; and because the pronoun of a single [entity] may refer to it, as you say “kilā al-rajulayni jāʾa” (both of the two men came [sg.]); Allah, the Exalted, said: «Both of the two gardens brought forth their produce» (Qurʾān, Sūrat al-Kahf 18:33); and because the alif is obligatory in all three states when it is annexed to an explicit noun; and because its imāla is permissible, whereas the dual does not admit imāla."},
    {"type": "pair",
     "ar": "وألفه بدل من الواو لإبدال التاء منها في المؤنث، ولم تبدل التاء من الياء إلا في اثنتين. وقال السيرافي: بدل من الياء لسماع الإمالة، ولا يميلون اسما ثلاثيا على غير الشذوذ، إلا ما كان من ذوات الياء.",
     "en": "Its alif is a substitute for a wāw, because the tāʾ is substituted for it in the feminine [kiltā]; and the tāʾ is not substituted for a yāʾ except in ithnatān (two, fem.). Al-Sīrāfī said: [the alif] is a substitute for a yāʾ, on account of imāla being heard [in it]; and they do not incline a trilateral noun, save anomalously, except what is of the yāʾ-radical class."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "التاء بدل من الألف، والألف للتأنيث؛ لأن علامة التأنيث لا تكون متوسطة، وما أضيف إلى كلا وكلتا يجب أن يكون مثنى أو ضميره، وما يضاف إليه لا يكون متعددا غير مثنى، إلا ما في الشعر كقولك: كلا زيد وعمرو،",
     "en": "The tāʾ [in kiltā] is a substitute for the alif, and the alif is for the feminine, because the feminine marker cannot be medial. What is annexed to kilā and kiltā must be a dual or its pronoun, and what it is annexed to cannot be a plural that is non-dual — save what occurs in poetry, as your saying “kilā Zaydin wa-ʿAmrin” (both Zayd and ʿAmr)."},
    {"type": "pair",
     "ar": "وإلحاق التاء بكلا مضافا إلى المؤنث أفصح من تجريده. واختلف في ألف «كلا» أنه في الأصل واو أو ياء، والأكثرون على الأول.",
     "en": "Appending the tāʾ to kilā, when it is annexed to a feminine, is more eloquent than leaving it bare. There is disagreement as to whether the alif of kilā is originally a wāw or a yāʾ, and the majority hold the former [a wāw]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: اعتبار اللفظ واعتبار المعنى.",
     "en": "That is: consideration of the wording and consideration of the meaning."},
]
