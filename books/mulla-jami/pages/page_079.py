# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 79 (printed ٧٨)."""

PAGE_NUMBER = 79
PRINTED_PAGE = "٧٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فإذا أضيف[[١]] إلى المظهر[[٢]] الذي هو الأصل، روعي جانب لفظه[[٣]] الذي هو الأصل، وأعرب بالحركات التي هي في الأصل، لكن تكون حركاته تقديرية؛ لأن آخره ألف تسقط بالتقاء الساكنين، نحو: «جاءني كلا الرجلين»، و«رأيت كلا الرجلين»، و«مررت بكلا الرجلين».",
     "en": "So when it is annexed to an overt noun (al-muẓhar) — which is the base (al-aṣl) — the aspect of its wording, which is the base, is taken into account, and it is inflected with the [short] vowels that are original; yet its vowels are estimated (taqdīrī), because its ending is an alif which is elided when two quiescents meet, as in: “jāʾanī kilā al-rajulayni” (both men came to me), “raʾaytu kilā al-rajulayni” (I saw both men), and “marartu bi-kilā al-rajulayni” (I passed by both men)."},
    {"type": "matn",
     "ar": "وإذا أضيف إلى المضمر الذي هو الفرع[[٤]]، روعي جانب معناه الذي هو الفرع، وأعرب بالحروف التي هي الفرع، نحو: «جاءني كلاهما»، و«رأيت كليهما»، و«مررت بكليهما»، فلذلك قيد كون إعرابه بالحروف بكونه مضافا إلى مضمر[[٥]].",
     "en": "And when it is annexed to a pronoun (al-muḍmar) — which is the derivative (al-farʿ) — the aspect of its meaning, which is the derivative, is taken into account, and it is inflected with letters (ḥurūf), which are the derivative, as in: “jāʾanī kilāhumā” (both of them came to me), “raʾaytu kilayhimā” (I saw both of them), and “marartu bi-kilayhimā” (I passed by both of them). It is for this reason that [the author] restricted its being inflected with letters to its being annexed to a pronoun."},
    # NOTE: printed marker [٥] sits on the phrase "مضافا إلى مضمر" of the sentence above.
    {"type": "matn",
     "ar": "(واثنان) وكذا «اثنتان» و«ثنتان»[[٦]]، فإن هذه الألفاظ وإن كانت مفردة، لكن صورتها صورة التثنية، ومعناها معنى التثنية[[٧]]، فألحقت بها (بالألف[[٨]]) رفعا (والياء) المفتوح ما قبلها نصبا وجرا، كما سيجيء.",
     "en": "(And ithnāni [two]) — and likewise “ithnatāni” and “thintāni” — for these words, though singular [in coinage], nevertheless have the form of the dual and the meaning of the dual; hence they are attached to it [the dual] (by the alif) in the nominative (and the yāʾ), that which precedes it bearing a fatḥa, in the accusative and genitive, as will come [later]."},
    {"type": "matn",
     "ar": "(جمع المذكر السالم) والمراد به: ما سمي به اصطلاحا. وهو الجمع بالواو والنون، أو بالياء والنون. فيدخل فيه[[٩]] نحو: «سنين وأرضين» مما لا يكون واحده مذكرا، يجمع بالواو والنون.",
     "en": "(The sound masculine plural [jamʿ al-mudhakkar al-sālim]) — what is intended by it is that which is so named by convention (iṣṭilāḥan). It is the plural [formed] with wāw and nūn, or with yāʾ and nūn. There enters under it [instances] such as “sinīn” (years) and “araḍīn” (lands), among that whose singular is not masculine, [yet] is pluralized with wāw and nūn."},
    {"type": "matn",
     "ar": "(و) ما ألحق به وهو (أولو) جمع «ذو»[[١٠]] لا عن لفظه (وعشرون وأخواتها[[١١]])",
     "en": "(And) that which is attached to it, namely (ulū) — the plural of “dhū,” though not from its own wording — (and ʿishrūna [twenty] and its sisters)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كلا وكلتا.",
     "en": "[The subject is] kilā and kiltā."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يجب في هذا المظهر أن يكون معرفة.",
     "en": "It is necessary that this overt noun be definite (maʿrifa)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لفظ «كلا».",
     "en": "That is: the wording “kilā.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: إنه إذا كان مضافا إلى المضمر، فالأغلب كونه جاريا على المثنى، وهو موافق له لفظا ومعنى.",
     "en": "It has been said: when it is annexed to a pronoun, then most often it is in apposition to (jāriyan ʿalā) a dual, and it agrees with it in wording and meaning."},
    {"type": "pair",
     "ar": "وأصل المثنى أن يكون معربا، فالأولى جعله موافقا لمتبوعه في الإعراب، ثم اطرد ذلك فيما إذا لم يتبع المثنى المعرب، نحو: جئنا كلانا،",
     "en": "The default (aṣl) of the dual is that it be declined (muʿrab); so it is preferable to make it [kilā] concordant with its antecedent (matbūʿ) in inflection. Then this became regular even where it does not follow a declined dual, as in “jiʾnā kilānā” (we came, both of us);"},
    {"type": "pair",
     "ar": "وأما إذا أضيف إلى المظهر، فإنه لا يجري على المثنى أصلا.",
     "en": "but when it is annexed to an overt noun, then it is not in apposition to a dual at all."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يخفى أنه مستدرك لا طائل تحته.",
     "en": "It is not hidden that this is a redundant qualification (mustadrak) with no benefit beneath it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لفظان موضوعان لمؤنث اثنان، لأن التاء فيهما ليست لتأنيث، إذ تاء التأنيث لا تلحق في وسط الكلمة.",
     "en": "[They are] two words coined for the feminine of “ithnāni,” for the tāʾ in them is not for feminization, since the tāʾ of feminization is not affixed in the middle of a word."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأنه تكرار الوحدة مرة.",
     "en": "Because it is the [single] repetition of the unit [i.e., the unit taken twice]."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: بالتثنية.",
     "en": "That is: [it is attached] to the dual."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: في الجمع.",
     "en": "That is: under [the category of] the plural."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "فلا يكون جمعا سالما لوجوب أن يكون مفرده معربا عن لفظه. وكذا أولات جمع ذات لا عن لفظها، فلا يكون جمع المؤنث السالم، فينبغي أن يذكر أولات مع جمع المؤنث السالم ملحقا به.",
     "en": "So it is not a sound plural, because [a sound plural] requires that its singular be declined from its own wording. Likewise “ulāt” is the plural of “dhāt,” not from its wording, so it is not [itself an instance of] the sound feminine plural; hence “ulāt” ought to be mentioned together with the sound feminine plural as attached to it."},
    {"type": "pair",
     "ar": "وأما ذوو فهو جمع سالم، فلذا لم يعده من ملحقاته.",
     "en": "As for “dhawū” [the plural of dhū], it is a sound plural, and so he did not count it among its appendages."},
    {"type": "pair",
     "ar": "وإنما قدم أولو على عشرين لأنه جمع، ولا يدل على عدد معين، كما هو مقتضى الجمع.",
     "en": "He only placed “ulū” before “ʿishrūn” because it is a plural and does not indicate a specific number, as is the requirement of the plural."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "المراد بالأخت المثل على ما أشار إليه بقوله: ونظائرها السبع، وبه فسر التنزيل حيث فسر ﴿كلما دخلت أمة لعنت أختها﴾ (سورة الأعراف:٣٨).",
     "en": "What is intended by “sister” (ukht) is “the like / counterpart” (al-mithl), in accordance with what he pointed to by his words — and its analogues are the seven [i.e., thirty through ninety]; and by it the Revelation was interpreted, where His words were explained: “Every time a nation enters, it curses its sister [nation]” (Qurʾān, Sūrat al-Aʿrāf 7:38)."},
    {"type": "pair",
     "ar": "فاستعارة الأخت للمثل استعارة عربية غير مصنوعة للنحاة.",
     "en": "So the metaphor of “sister” for “the like” is a natural Arabic metaphor, not one fashioned by the grammarians."},
]
