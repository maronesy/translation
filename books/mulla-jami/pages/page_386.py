# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 386 (printed ٣٨٥)."""

PAGE_NUMBER = 386
PRINTED_PAGE = "٣٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # A new lemma begins at the head of the page; no heading is printed.
    {"type": "matn",
     "ar": "(و«ما» الاسمية[[١]]) لا الحرفية[[٢]]، فإنها: إما كافة[[٣]] نحو: «إنما زيد قائم»، وإما نافية نحو: «ما ضربت زيدا، وما زيد قائما».",
     "en": "(And nominal “mā”), not the particle mā, for that is either restraining (kāffa), as in “innamā Zaydun qāʾimun” (Zayd is only standing), or negating, as in “mā ḍarabtu Zaydan” (I did not strike Zayd) and “mā Zaydun qāʾiman” (Zayd is not standing)."},
    {"type": "matn",
     "ar": "(موصولة) نحو: «عرفت ما اشتريته».",
     "en": "(Is relative) (mawṣūla), as in “ʿaraftu mā ishtaraytuhu” (I knew what I had bought)."},
    {"type": "matn",
     "ar": "(واستفهامية[[٤]]) نحو: «ما عندك؟ وما فعلت؟».",
     "en": "(And interrogative) (istifhāmiyya), as in “mā ʿindaka?” (what do you have?) and “mā faʿalta?” (what did you do?)."},
    {"type": "matn",
     "ar": "(وشرطية) نحو: «ما تصنع أصنع».",
     "en": "(And conditional) (sharṭiyya), as in “mā taṣnaʿ aṣnaʿ” (whatever you do, I shall do)."},
    {"type": "matn",
     "ar": "(وموصوفة) إما بمفرد نحو: «مررت بما معجب لك» أي: بشيء يعجبك.",
     "en": "(And qualified) (mawṣūfa), either by a single word, as in “marartu bi-mā muʿjibin laka” (I passed by something pleasing to you), that is, by a thing that pleases you;"},
    {"type": "matn",
     "ar": "وإما بجملة نحو:",
     "en": "or by a sentence, as in:"},
    {"type": "verse",
     "ar": "ربما تكره النفوس[[٥]] من الأمر     له فرجة كحل العقال",
     "en": "Many a thing [in the course] of affairs the souls dislike / has a release for it like the loosing of a hobble,"},
    {"type": "matn",
     "ar": "أي: رب شيء تكرهه النفوس.",
     "en": "that is, “many a thing that the souls dislike”."},
    {"type": "matn",
     "ar": "(وتامة[[٦]] بمعنى «شيء») منكر عند أبي علي، و«الشيء» المعرف عند سيبويه،",
     "en": "(And complete) (tāmma) (in the sense of “a thing”), indefinite according to Abū ʿAlī, and “the thing”, definite, according to Sībawayh,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿فنعما هي﴾[[٧]] أي: نعم شيئا، أو نعم الشيء هي",
     "en": "as in His words, the Exalted: “fa-niʿimmā hiya” (it is excellent), that is, “an excellent thing it is”, or “excellent is the thing, it”."},
    {"type": "matn",
     "ar": "(وصفة[[٨]]) نحو: «اضربه",
     "en": "(And a qualifier) (ṣifa), as in “iḍribhu…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لما كان في المبنيات ما يوافق لفظه لفظ الموصول لم يجعل له باب برأسه، بل بين في ضمن الموصولات،",
     "en": "Shaykh al-Raḍī said: since among the indeclinables there is what agrees in form with the relative noun, no chapter of its own was made for it; rather it was explained within [the chapter of] the relative nouns,"},
    {"type": "pair",
     "ar": "كما بين ما وافق اسم الفعل في اللفظ من المبنيات في أسماء الأفعال كفجار وفساق وباب قطام الموافقة لباب نزال.",
     "en": "just as the indeclinables that agree in form with the verbal noun (ism al-fiʿl) were explained among the verbal nouns, such as fajāri and fasāqi and the pattern of qaṭāmi, which agree with the pattern of nazāli."},
    {"type": "pair",
     "ar": "ولولا قصد الاختصار ورعاية المناسبة اللفظية لكان القياس يقتضي أن تجعل أبوابا برأسها.",
     "en": "Were it not for the aim of brevity and regard for formal correspondence, analogy would require that they be made chapters of their own."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه ذاكر أحوال الاسم. وأما أقسام الحرفية، فسيجيء في بحثه.",
     "en": "Because he is setting out the states of the noun. As for the kinds of the particle [mā], they will come in their own discussion."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: مثلا.",
     "en": "That is: for example."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قد يزاد معها التحقير والتعظيم والإنكار.",
     "en": "Belittling, magnifying and disapproval are sometimes added along with it."},
    {"type": "pair",
     "ar": "ويحذف ألف «ما» الاستفهامية في الأغلب عند كونها مجرورة بحرف جر أو مضافا إلا إذا جاء «ذا» بعد «ما» الاستفهامية نحو: بماذا تشتغل.",
     "en": "The alif of interrogative “mā” is mostly elided when it is governed in the genitive by a preposition or by an annexed noun, unless “dhā” comes after interrogative “mā”, as in “bi-mādhā tashtaghilu?” (with what are you occupied?)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: جاز أن يكون «ما» كافة.",
     "en": "It has been said: “mā” may be restraining (kāffa)."},
    # REVIEW: «مقامهن» printed (one expects «مقامه»); transcribed as printed.
    {"type": "pair",
     "ar": "قال المصنف: إلا أن النحاة اختاروا كونها موصوفة لئلا يلزم حذف الموصوف، وإقامة الجار والمجرور مقامهن يعني: قوله من الأمر وذلك قليل إلا بشرط.",
     "en": "The author said: but the grammarians preferred its being qualified, so that it does not entail elision of the qualified noun and putting the preposition and its object in its place—he means his words “min al-amr”—and that is rare except under a condition."},
    {"type": "pair",
     "ar": "وفيه أنه يجوز أن يكون «من» للتبعيض متعلقة بـ«تكره» كما في «أخذت من الدراهم» أي: شيئا من الدراهم.",
     "en": "Against this: “min” may be partitive, attached to “takrahu”, as in “akhadhtu min al-darāhim” (I took of the dirhams), that is, something of the dirhams."},
    {"type": "pair",
     "ar": "ويجوز أيضا تضمين تكره معنى تشمئز وتنقبض.",
     "en": "It is also possible for “takrahu” to be made to include the sense of “tashmaʾizzu” (shrinks in aversion) and “tanqabiḍu” (recoils)."},
    {"type": "pair",
     "ar": "وجملة قوله له فرجة صفة للأمر لأن اللام فيه للعهد الذهني.",
     "en": "The sentence “lahu farjatun” is a qualifier of “al-amr”, because its definite article is for mental reference (al-ʿahd al-dhihnī)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: «محتاجة» printed; the sense of «تامة» calls for «غير محتاجة»; transcribed as printed.
    {"type": "pair",
     "ar": "قيل: أي: محتاجة إلى صلة أو صفة.",
     "en": "It has been said: that is, needing [as printed; the sense requires “not needing”] a relative clause or a qualifier."},
    {"type": "pair",
     "ar": "قلت: أو موصوف وقوله: بمعنى شيء صفة التامة ذكره تنصيصا على اختيار مذهب أبي علي دون سيبويه.",
     "en": "I say: or a qualified noun. His words “in the sense of a thing” are a qualifier of “complete”; he mentioned it to state explicitly that he prefers the doctrine of Abū ʿAlī rather than that of Sībawayh."},
    {"type": "pair",
     "ar": "ولك أن تجعله بيان المعاني ما سوى الموصولة، ويحصل الفائدة السابقة ضمنا.",
     "en": "You may also make it an explanation of the meanings of mā other than the relative, and the foregoing point is then obtained implicitly."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:271."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: «اختلفت» printed (one expects «اختلف» or «اختلفوا»); transcribed as printed.
    {"type": "pair",
     "ar": "اختلفت في «ما» التي تلي النكرة لإفادة الإبهام، فقال بعضهم: إنه حرف. وقال بعضهم: إنه اسم،",
     "en": "There is disagreement about the “mā” that follows an indefinite noun to convey vagueness: some said it is a particle, and some said it is a noun."},
    {"type": "pair",
     "ar": "وفائدتها إما التحقير أو التعظيم أو التنويع نحو: «أعطيت عطية ما» أي: عطية لا تعرف من حقارتها،",
     "en": "Its function is belittling, magnifying or specifying a kind, as in “aʿṭaytu ʿaṭiyyatan mā” (I gave a gift of some sort), that is, a gift unrecognizable for its paltriness;"},
    {"type": "pair",
     "ar": "ولأمر ما أي: لأمر عظيم لا يعرف من عظمته، واضربه ضربا ما أي: ضربا مجهولا غير معين.",
     "en": "“li-amrin mā” (for some matter), that is, for a great matter unrecognizable for its greatness; and “iḍribhu ḍarban mā” (strike him with some sort of striking), that is, an unknown, unspecified striking."},
]
