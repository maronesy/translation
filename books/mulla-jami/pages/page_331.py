# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 331 (printed ٣٣٠)."""

PAGE_NUMBER = 331
PRINTED_PAGE = "٣٣٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «تكون أجنبية بالنسبة إلى الموصوف، فلا» at the foot of PDF p. 330.
    {"type": "matn",
     "ar": "يصح أن تقع صفة له مثل: «جاءني رجل زيد عالم».",
     "en": "…soundly occur as an adjective of it, as in “A man came to me—Zayd is learned.”"},
    {"type": "matn",
     "ar": "(ويوصف بحال الموصوف[[١]]) أي: بحال قائمة به (نحو: «مررت برجل حسن»)؛ إذ الحسن حال الرجل وصفته",
     "en": "(A thing is qualified by a state of the qualified itself), that is, by a state subsisting in it, (as in “I passed by a handsome man”), since handsomeness is the man’s state and attribute;"},
    {"type": "matn",
     "ar": "(وبحال متعلقه[[٢]]) أي: متعلق الموصوف، يعني: بصفة اعتبارية[[٣]] يحصل له بسبب متعلقه",
     "en": "(and by a state of what is connected with it (mutaʿalliqihi)), that is, of what is connected with the qualified, meaning by a notional attribute (ṣifa iʿtibāriyya) that belongs to it by reason of what is connected with it,"},
    {"type": "matn",
     "ar": "(نحو: «مررت برجل حسن غلامه»)؛ إذ كون الرجل حسن الغلام معنى فيه، وإن كان اعتباريا.",
     "en": "(as in “I passed by a man whose slave is handsome”), since the man’s being one whose slave is handsome is a meaning in him, even if notional."},
    {"type": "matn",
     "ar": "(فالأول) أي: النعت بحال الموصوف (يتبعه) أي: الموصوف في عشرة أمور يوجد منها في كل تركيب أربعة",
     "en": "(The first), that is, the qualifier by a state of the qualified, (follows it), that is, the qualified, in ten things, four of which are found in every construction:"},
    {"type": "matn",
     "ar": "(في الإعراب) رفعا ونصبا وجرا (والتعريف والتنكير[[٤]]، والإفراد والتثنية والجمع، والتذكير والتأنيث[[٥]])",
     "en": "(in inflection), nominative, accusative and genitive; (in definiteness and indefiniteness; in singular, dual and plural; and in masculine and feminine);"},
    {"type": "matn",
     "ar": "إلا إذا كان صفة يستوي فيها المذكر والمؤنث، كـ«فعول» بمعنى: «فاعل» نحو: «رجل صبور» و«امرأة صبور»",
     "en": "except when it is an adjective in which masculine and feminine are alike, such as faʿūl in the sense of fāʿil, as in “a patient man” (rajul ṣabūr) and “a patient woman” (imraʾa ṣabūr),"},
    {"type": "matn",
     "ar": "أو «فعيل» بمعنى «مفعول» كـ«رجل جريح» و«امرأة جريح» أو كان صفة مؤنثة تجري على المذكر كـ«علامة».",
     "en": "or faʿīl in the sense of mafʿūl, as in “a wounded man” (rajul jarīḥ) and “a wounded woman” (imraʾa jarīḥ); or when it is a feminine adjective applied to the masculine, such as “ʿallāma” (very learned)."},
    {"type": "matn",
     "ar": "(والثاني) أي: النعت بحال متعلق الموصوف (يتبعه في الخمسة الأول) وهي: «الرفع والنصب والجر، والتعريف والتنكير» ويوجد منها في كل تركيب اثنان.",
     "en": "(The second), that is, the qualifier by a state of what is connected with the qualified, (follows it in the first five), namely “nominative, accusative and genitive, definiteness and indefiniteness,” two of which are found in every construction."},
    {"type": "matn",
     "ar": "(وفي البواقي) من تلك الأمور العشرة، وهي أيضا خمسة: «الإفراد والتثنية والجمع والتذكير والتأنيث» (كالفعل) لشبهه به،",
     "en": "(And in the remaining ones) of those ten things—they too are five: “singular, dual and plural, masculine and feminine”—(it is like the verb), because of its resemblance to it."},
    {"type": "matn",
     "ar": "يعني: ينظر إلى فاعله، فإن كان مفردا أو مثنى أو مجموعا أفرد كما يفرد الفعل،",
     "en": "That is, one looks to its agent (fāʿil): if it is singular, dual or plural, [the qualifier] is put in the singular, as the verb is put in the singular;"},
    {"type": "matn",
     "ar": "وإن كان مذكرا أو مؤنثا حقيقيا بلا فصل طابقه وجوبا كما يطابق الفعل فاعله في التذكير والتأنيث،",
     "en": "if it is masculine, or genuinely feminine with no intervening separation, it agrees with it obligatorily, as the verb agrees with its agent in masculine and feminine;"},
    {"type": "matn",
     "ar": "وإن كان فاعله مؤنثا غير حقيقي أو حقيقيا مفصولا يذكر أو يؤنث جوازا",
     "en": "and if its agent is non-genuinely feminine, or genuinely feminine but separated, it may optionally be masculine or feminine."},
    {"type": "matn",
     "ar": "تقول: «مررت برجل قاعد غلامه» مثل: «يقعد غلامه» و«برجلين قاعد غلاماهما» مثل: «يقعد غلاماهما» و«برجال قاعد غلمانهم»",
     "en": "You say “I passed by a man whose slave is sitting” (bi-rajulin qāʿidin ghulāmuhu), like “his slave sits” (yaqʿudu ghulāmuhu); “by two men whose two slaves are sitting” (bi-rajulayni qāʿidin ghulāmāhumā), like “their two slaves sit” (yaqʿudu ghulāmāhumā); and “by men whose slaves are sitting” (bi-rijālin qāʿidin ghilmānuhum)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الجار والمجرور مفعول ما لم يسم فاعله.",
     "en": "The preposition and its object stand as the object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المتعلق أعم من أن يكون ما له إضافة ونسبة إليه كالأب والغلام، أو ما له ربط إلى ما له تلك النسبة كقولك: قام رجل ضارب أباه زيد.",
     "en": "“What is connected” is more general than what has annexation and relation to it, like the father and the slave; it includes what has a link to that which has such a relation, as when you say “A man stood up whose father Zayd is striking.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما يصح الوصف بها؛ لأنها بمنزلة حالة باعتبار نفسه في حصول الفائدة.",
     "en": "Description by it is sound only because, as regards yielding benefit, it stands in the place of a state considered with respect to the [qualified] itself."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جوز الكوفيون وصف النكرة مطلقا بالمعرفة، والأخفش وصف النكرة المخصوصة بها.",
     "en": "The Kūfans permitted qualifying the indefinite by the definite without restriction, and al-Akhfash permitted qualifying a specified indefinite by it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: print reads «رجل عدل، ورجل عدل، وامرأة عدل» with «رجل عدل» repeated; a dual/plural example (e.g. «رجلان عدل») may be intended; transcribed as printed.
    {"type": "pair",
     "ar": "إلا إذا كان مصدرا، فإنه يستوي فيه جميع هذه الأمور، نحو: رجل عدل، ورجل عدل، وامرأة عدل،",
     "en": "Except when it is a verbal noun (maṣdar), for all these things are alike in it, as in “a just man” (rajul ʿadl), “a just man,” and “a just woman” (imraʾa ʿadl);"},
    {"type": "pair",
     "ar": "أو أفعل التفضيل بـ«من»، فإنه مفرد مذكر، أو أفعل التفضيل المضاف للزيادة على من أضيف إليه،",
     "en": "or the elative (afʿal al-tafḍīl) with “min,” for it is singular masculine; or the elative annexed [and meant] for excess over those to whom it is annexed;"},
    {"type": "pair",
     "ar": "أو فعولا بمعنى فاعل، نحو: رجل صبور وامرأة صبور، أو فعيلا بمعنى مفعول كرجل جريح وامرأة جريح،",
     "en": "or faʿūl in the sense of fāʿil, as in “a patient man” and “a patient woman”; or faʿīl in the sense of mafʿūl, as in “a wounded man” and “a wounded woman.”"},
    {"type": "pair",
     "ar": "وما في الشروح في هذا المقام سهو بين وقع من هفوة الأقلام.",
     "en": "What is found in the commentaries on this point is a clear oversight arising from a slip of the pen."},
]
