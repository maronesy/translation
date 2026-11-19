# -*- coding: utf-8 -*-
"""
Mulla Jami — al-Fawa'id al-Diya'iyya (commentary on al-Kafiya of Ibn al-Hajib)
Source page: 26 of the PDF  (printed page ٢٥) — continuation of the Introduction.

Block types:
  khutba – the opening authorial address (matn), ar + en
  matn   – a sentence of the base text (matn), ar + en
  note   – opens a numbered footnote (num + optional label)
  pair   – a sentence pair inside the current footnote, ar + en
  rule   – a decorative divider
"""

PAGE_NUMBER = 26          # PDF page
PRINTED_PAGE = "٢٥"       # page number printed in the book

BLOCKS = [
    # ---------------- The base text (matn / khutba) ----------------
    {"type": "khutba",
     "ar": "الله تعالى بغفرانه[[١]]، وأسكنه بحبوحة[[٢]] جنانه-،",
     "en": "—may God the Exalted [envelop him] in His forgiveness, and lodge him in the midmost of His gardens—"},
    {"type": "khutba",
     "ar": "نظمتها[[٣]] في سلك التقرير، وسمط التحرير[[٤]]،",
     "en": "I have strung them upon the thread of exposition and the necklace-cord of composition,"},
    {"type": "khutba",
     "ar": "للولد العزيز ضياء الدين[[٥]] يوسف[[٦]]، -حفظه[[٧]] الله سبحانه[[٨]] وتعالى عن موجبات التلهف والتأسف[[٩]]-،",
     "en": "for [my] dear son Ḍiyāʾ al-Dīn Yūsuf—may God, Glorified and Exalted is He, preserve him from the causes of grief and regret—"},
    {"type": "khutba",
     "ar": "وسميتها[[١٠]] بـ«الفوائد",
     "en": "and I have named them “al-Fawāʾid"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال في الحاشية: التغمد: الستر، انتهى.",
     "en": "In the gloss it is said: “al-taghammud” means covering — end [of quotation]."},
    {"type": "pair",
     "ar": "يعني: ستر الله ما كان منه بغفرانه اللائق بجنابه، أو الناشئ من محض فضله من غير سابقية العمل.",
     "en": "That is: may God cover over what proceeded from him, by His forgiveness befitting His majesty — or [His forgiveness] arising from His sheer bounty, without any antecedent [meritorious] deed."},
    {"type": "pair",
     "ar": "ويجوز أن يجعل كناية عن الإحاطة، أي: أحاط الله بغفرانه وجعله شاملا له.",
     "en": "It may also be taken as a metonymy for encompassment, that is: may God encompass him with His forgiveness and make it comprehend him wholly."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "البحبوحة: -بضم الباء- الوسط، وهو نصب على الظرفية.",
     "en": "“Al-buḥbūḥa” — with a ḍamma on the [first] bāʾ — means the middle; it is accusative as an adverb of place (ẓarf)."},
    {"type": "pair",
     "ar": "والجنان -بالكسر- جمع جنة -بالفتح-، وهي في الأصل حديقة ذات أشجار ونخيل.",
     "en": "“Al-jinān” — with a kasra — is the plural of “janna” — with a fatḥa — which originally means a garden with trees and palms."},
    {"type": "pair",
     "ar": "بحبوحة الدار وسطها، ومن كل شيء وسطه وخياره.",
     "en": "The “buḥbūḥa” of a dwelling is its middle, and of anything it is its center and its choicest part."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يقال: نظمت اللؤلؤ، أي: جمعتها في سلك.",
     "en": "One says: “I strung the pearls (naẓamtu al-luʾluʾ),” that is: I gathered them on a thread."},
    {"type": "pair",
     "ar": "وهي صفة ثانية لـ«فوائد»، وضميرها للفوائد.",
     "en": "It [“naẓamtuhā”] is a second adjectival [clause] qualifying “fawāʾid,” and its pronoun refers back to the fawāʾid."},
    {"type": "pair",
     "ar": "فكأنه شبه الفوائد المنتشرة بالدرر والجواهر، سواء كان المراد منها الألفاظ الدالة على المعاني، أو المعاني المدلولة عن الألفاظ.",
     "en": "It is as though he likened the scattered fawāʾid to pearls and gems — whether what is intended by them is the expressions that signify meanings, or the meanings signified by the expressions."},
    {"type": "pair",
     "ar": "وشبه ترتيب الألفاظ الدالة على المعاني، أو ترتيب نفس المعاني، بالنظم.",
     "en": "And he likened the ordering of the expressions signifying the meanings — or the ordering of the meanings themselves — to a stringing [of pearls] (naẓm)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "والسلك: الخيط.",
     "en": "“Al-silk” is the thread."},
    {"type": "pair",
     "ar": "والتقرير: جعل الشيء في قراره، أو الحمل على الإقرار. والحمل على الثاني أبلغ في مدح الكتاب.",
     "en": "“Al-taqrīr” is setting a thing firmly in its resting-place, or bringing [one] to acknowledgment (iqrār); taking it in the second sense is more emphatic in praising the book."},
    {"type": "pair",
     "ar": "والسمط: السلك ما دام فيه الخرز، وإلا فهو سلك.",
     "en": "“Al-simṭ” is a cord so long as the beads are strung on it; otherwise it is [merely] a thread (silk)."},
    {"type": "pair",
     "ar": "والتحرير: التقويم. وفي إضافة السمط إلى التحرير إشارة إلى أن تحريره لا يفارق الفوائد التي كاللآلئ.",
     "en": "“Al-taḥrīr” is setting straight, refining (taqwīm); and in annexing “al-simṭ” to “al-taḥrīr” there is an indication that his refined composition does not part from the fawāʾid, which are like pearls."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا لقبه، عطف بيان، أو بدل منه، والثاني هو الأولى.",
     "en": "This [“Ḍiyāʾ al-Dīn”] is his honorific title (laqab): [it is] an explicative apposition, or a substitute (badal) for it; and the second is preferable."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يجوز فيه الإعراب الثلاثة. والجر أولى لسلامته عن الحذف.",
     "en": "The three case-inflections are permissible in it; the genitive is preferable, as it is free of any ellipsis."},
    {"type": "pair",
     "ar": "إما بالبدلية عن الولد، أو بعطف البيان عنه.",
     "en": "[This is] either by way of substitution (badal) for “al-walad” (the son), or by explicative apposition to it."},
    {"type": "pair",
     "ar": "وضياء الدين لقب ولده، ويوسف اسمه.",
     "en": "“Ḍiyāʾ al-Dīn” is his son’s honorific title, and “Yūsuf” is his given name."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: يوسف.",
     "en": "That is: Yūsuf."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "نصب على المصدرية، وعامله محذوف وجوبا؛ لأنه بدل عنه، وهو علم جنس للتسبيح.",
     "en": "[“Subḥānahu” is] accusative as an absolute object (maṣdar); its governing verb is necessarily elided, since it stands as a substitute for it, and it is a generic proper name (ʿalam jins) for glorification (tasbīḥ)."},
    {"type": "pair",
     "ar": "وإضافته لا تبطل علميته لكونها لمجرد الإيضاح، كما في حاتم طي.",
     "en": "Its annexation does not nullify its status as a proper name, since the annexation is merely for clarification — as in “Ḥātim of Ṭayy.”"},
    {"type": "pair",
     "ar": "وقال الرضي: لا دليل على علميته؛ لأن أكثر ما يستعمل مضافا.",
     "en": "Al-Raḍī said: there is no proof of its being a proper name, since it is most often used in the annexed state."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "كلاهما بمعنى الحزن.",
     "en": "Both [“al-talahhuf” and “al-taʾassuf”] mean grief."},
    {"type": "pair",
     "ar": "وجمع الألفاظ المترادفة في الخطب جائز، بل قد يورث حسنا.",
     "en": "Combining synonymous words in orations is permissible — indeed, it may impart beauty."},
    {"type": "pair",
     "ar": "وقيل: التلهف: الحزن بسبب إتيان فعل لا بد من تركه.",
     "en": "It is said: “al-talahhuf” is grief on account of committing an act that ought to have been left undone,"},
    {"type": "pair",
     "ar": "والتأسف: الحزن بسبب ترك فعل لا بد من الإتيان به.",
     "en": "while “al-taʾassuf” is grief on account of omitting an act that ought to have been performed."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: التلهف: الحسرة والحزن على فوات المطلوب. والتأسف: الحسرة والحزن على نزول المكروه.",
     "en": "ʿAbd al-Ḥakīm said: “al-talahhuf” is regret and grief over the loss of something desired, while “al-taʾassuf” is regret and grief over the befalling of something disliked."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: سميت الفوائد التي نظمتها، عطف على «نظمتها»، والتسمية تتعدى إلى مفعولين بنفسها، نحو: «سميت ابني زيدا»،",
     "en": "That is: “I named the fawāʾid that I have strung” — [the verb “I named”] is coordinated with “I strung”; and naming (tasmiya) governs two objects directly, as in “I named my son Zayd,”"},
    {"type": "pair",
     "ar": "وتتعدى إلى الثاني بالباء، نحو: «سميت ابني بزيد»، وههنا من القسم الثاني.",
     "en": "and it [also] governs the second object by means of the preposition bi-, as in “I named my son by [the name] Zayd”; and here it is of the second kind."},
]
