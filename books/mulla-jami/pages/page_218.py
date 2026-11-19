# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 218 (printed ٢١٧)."""

PAGE_NUMBER = 218
PRINTED_PAGE = "٢١٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "النصب أو البناء، فلم يرد عليه الترخيم الذي هو من خصائص المنادى،",
     "en": "…the accusative or the indeclinable ending; so curtailment, which is a property of the vocative, does not apply to it."},
    {"type": "matn",
     "ar": "ولا مفتوحا بزيادة الألف؛ لأن الزيادة تنافي الحذف،",
     "en": "Nor [may it be] given a fatḥa through the addition of the alif, because addition is incompatible with elision."},
    {"type": "matn",
     "ar": "ولم يذكر المندوب؛ لأنه غير داخل في المنادى عنده، وما وقع في بعض النسخ: «ولا مندوبا» فكأنه من تصرف الناسخين،",
     "en": "He did not mention the lamented noun (al-mandūb), because in his view it is not included in the vocative; and what occurs in some copies—“nor lamented”—seems to be the copyists’ doing,"},
    {"type": "matn",
     "ar": "مع أن وجه اشتراطه عند دخوله في المنادى ظاهر، وهو أن الأغلب فيه زيادة الألف في آخره لمد الصوت إظهارا للتفجع، فلا يناسبه الترخيم الذي للتخفيف.",
     "en": "although the reason for this condition, were it included in the vocative, is evident: mostly an alif is added at its end to prolong the voice in display of grief, so curtailment, which is for lightening, does not suit it."},
    {"type": "matn",
     "ar": "٣-(و) أن (لا) يكون (جملة[[١]])؛ لأن الجملة محكية بحالها فلا تتغير.",
     "en": "3. (And) that it (not) be (a sentence), because a sentence [used as a name] is reported as it is and so does not change."},
    {"type": "matn",
     "ar": "٤-والشرط الرابع: أحد أمرين وجوديين (و) هو (أن يكون) المنادى:",
     "en": "4. The fourth condition is one of two positive things, (and) it is (that) the vocative (be):"},
    {"type": "matn",
     "ar": "(إما علما زائدا على ثلاثة أحرف)؛ لأنه لعلميته ناسبه التخفيف بالترخيم، لكثرة نداء العلم مع أنه لشهرته يكون فيما أبقى منه دليل على ما ألقي،",
     "en": "(either a proper name of more than three letters), because, being a proper name, lightening by curtailment suits it, since proper names are called on frequently; moreover, because it is well known, what is kept of it indicates what was dropped;"},
    {"type": "matn",
     "ar": "ولزيادته على الثلاثة لم يلزم نقص الاسم[[٢]] عن أقل أبنية المعرب بلا علة موجبة[[٣]].",
     "en": "and because it exceeds three [letters], the noun is not reduced below the smallest pattern of the declinable noun without a necessitating cause."},
    {"type": "matn",
     "ar": "(وإما) اسما متلبسا (بتاء التأنيث[[٤]]) وإن لم يكن علما ولا زائدا على الثلاثة؛",
     "en": "(Or) a noun bearing (the tāʾ of the feminine), even if it is neither a proper name nor longer than three [letters],"},
    {"type": "matn",
     "ar": "لأن وضع التاء على الزوال، فيكفيه أدنى مقتض للسقوط، فكيف إذا وقع موقعا يكثر فيه سقوط الحرف الأصلي،",
     "en": "because the tāʾ is by origin set to be removable, so the slightest cause suffices for its dropping—all the more when it occurs in a position where even a root letter is often dropped."},
    {"type": "matn",
     "ar": "ولم يبالوا ببقاء نحو: «ثبة» و«شاة» بعد الترخيم على حرفين؛ لأن بقاءه كذلك ليس لأجل الترخيم، بل مع التاء أيضا كان ناقصا عن ثلاثة أحرف؛ إذ التاء كلمة أخرى برأسها،",
     "en": "They did not mind that such as “thuba” and “shāh” remain on two letters after curtailment, because its remaining so is not due to curtailment: even with the tāʾ it was short of three letters, since the tāʾ is a separate word in its own right."},
    {"type": "matn",
     "ar": "ولا يرخم بغير ضرورة منادى لم يستوف الشروط المذكورة إلا ما شذ من نحو: «يا صاح» في «يا صاحب» ومع شذوذه فالوجه في ترخيمه كثرة استعماله منادى.",
     "en": "Without necessity, a vocative that does not fulfil the stated conditions is not curtailed, except anomalous cases such as “yā ṣāḥi” for “yā ṣāḥibu”; and though it is anomalous, the reason for curtailing it is its frequent use as a vocative."},
    {"type": "matn",
     "ar": "ولما فرغ من بيان شرائط الترخيم شرع في بيان كمية[[٥]] المحذوف بسببه، فقال:",
     "en": "Having finished explaining the conditions of curtailment, he began to explain the quantity of what is elided through it, saying:"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بعض العرب يرخم الجملة بحذف عجزها نحو: يا تأبط.",
     "en": "Some Arabs curtail a sentence[-name] by dropping its latter part, as in “yā Taʾabbaṭa.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الذي في حكم المعرب، وإنما قيد به لجواز النقص فيما ليس في حكم المعرب، نحو: ما، ومن.",
     "en": "[That is, the noun] that has the status of the declinable. He qualified it so only because reduction is permitted in what does not have the status of the declinable, such as “mā” and “man.”"},
    {"type": "pair",
     "ar": "وأما نحو: يد، فالحذف فيه شاذ، والشاذ لا يعبأ به.",
     "en": "As for such as “yad,” the elision in it is anomalous, and the anomalous is not taken into account."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما قيد به لجواز النقص بالعلة الموجبة كعصا.",
     "en": "He qualified it so only because reduction is permitted through a necessitating cause, as in “ʿaṣan.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قد كثر الترخيم فيه، ولهذا عومل آخر غير المرخم منه في بعض المواضع معاملة المرخم، أعني: فتح التاء،",
     "en": "Curtailment is frequent in it; for this reason the end of an uncurtailed [noun] of this kind is in some places treated like the curtailed, I mean the tāʾ being given a fatḥa."},
    {"type": "pair",
     "ar": "وإذا وقف على ذلك المرخم ألحق آخره هاء السكت، فيقال في يا طلح يا طلحه،",
     "en": "When one pauses on that curtailed [noun], the hāʾ of silence is attached to its end; so for “yā Ṭalḥa” one says “yā Ṭalḥah.”"},
    {"type": "pair",
     "ar": "وذلك لأنهم يلحقون هاء السكت بآخر ما ليست حركته حركة إعرابية، ولا مشبهة بها، وقليل ما يوقف على السكون،",
     "en": "That is because they attach the hāʾ of silence to the end of a word whose vowel is not an inflectional vowel nor resembles one; pausing on the sukūn is rare."},
    {"type": "pair",
     "ar": "وقد يغني عن الهاء في الشعر ألف الإطلاق نحو: قفي قبل التفرق يا ضباعا.",
     "en": "In poetry the alif of prolongation (alif al-iṭlāq) may take the place of the hāʾ, as in: “Stop before parting, O Ḍubāʿā.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ويمكن أن يقال: شرع في أقسام الترخيم، أو شرع في بيان خصوصيات الترخيم بعد الفراغ من بيان شرائط مطلق الترخيم.",
     "en": "It may also be said: he began on the divisions of curtailment, or he began to explain the particulars of curtailment after finishing the conditions of curtailment in general."},
]
