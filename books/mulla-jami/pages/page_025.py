# -*- coding: utf-8 -*-
"""
Mulla Jami — al-Fawa'id al-Diya'iyya (commentary on al-Kafiya of Ibn al-Hajib)
Source page: 25 of the PDF  (printed page ٢٤) — continuation of the Introduction.

Block types:
  khutba – the opening authorial address (matn), ar + en
  matn   – a sentence of the base text (matn), ar + en
  note   – opens a numbered footnote (num + optional label)
  pair   – a sentence pair inside the current footnote, ar + en
  rule   – a decorative divider
"""

PAGE_NUMBER = 25          # PDF page
PRINTED_PAGE = "٢٤"       # page number printed in the book

BLOCKS = [
    # ---------------- The base text (matn / khutba) ----------------
    {"type": "khutba",
     "ar": "أما بعد[[١]]، فهذه[[٢]] فوائد[[٣]] وافية[[٤]] بحل[[٥]] مشكلات الكافية[[٦]]،",
     "en": "To proceed: these are ample notes (fawāʾid) that suffice for resolving the difficulties of al-Kāfiya,"},
    {"type": "khutba",
     "ar": "للعلامة[[٧]] لمشتهر[[٨]] في المشارق والمغارب[[٩]]، الشيخ[[١٠]] ابن الحاجب[[١١]]، -تغمده ........",
     "en": "[the work] of the erudite scholar (ʿallāma), of one renowned throughout the East and the West, Shaykh Ibn al-Ḥājib—may [God] envelop him ......."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كلمة «بعد» من الظروف اللازمة الإضافة التي بعد قطعها عن الإضافة. وتقدير ما أضيف إليها يبنى على الضم، وههنا كذلك.",
     "en": "The word “baʿd” is among the adverbs that necessarily take a genitive complement (muḍāf); once it is severed from that complement — with what would be annexed to it left merely implied — it is built on the ḍamma (indeclinable with final u), and such is the case here."},
    {"type": "pair",
     "ar": "والعامل فيه «أما»، لنيابتها عن الفعل؛ إذ أصل «أما بعد»: مهما يكن من شيء بعد الحمد والصلاة،",
     "en": "The element governing it is “ammā,” since it stands in place of the verb; for the underlying form of “ammā baʿdu” is: “whatever may occur after the praise and the blessing,”"},
    {"type": "pair",
     "ar": "فحذف «مهما يكن من شيء» وأقيم «أما» مقامه، كما تحذف الجملة ويقام «نعم» مقامها في قولنا: «نعم» لمن قال: «أقام زيد؟».",
     "en": "so “whatever may occur” was elided and “ammā” set in its place — just as a whole sentence is elided and “naʿam” (yes) set in its place, as in our saying “naʿam” to one who asks: “Did Zayd stand?”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: هذه الأمور الحاضرة في العقل، استحضر المعاني التي سيذكرها في كتابه على وجه الإجمال.",
     "en": "That is: these matters present in the mind — he has brought to presence the meanings that he will mention in his book, in summary fashion."},
    {"type": "pair",
     "ar": "وأورد اسم الإشارة لبيانها.",
     "en": "He employed the demonstrative pronoun in order to point them out."},
    {"type": "pair",
     "ar": "وأسماء الإشارة ربما تستعمل في الأمور المعقولة، وإن كان وضعها للأمور المبصرة الحاضرة في مرأى المخاطب، لكن لا بد من نكتة.",
     "en": "Demonstrative pronouns are sometimes used for intelligible matters, even though they were coined for visible things present before the addressee’s sight — yet this requires a subtle point (nukta)."},
    {"type": "pair",
     "ar": "والنكتة هنا إما الإشارة إلى إتقانه هذه المعاني حتى صارت لكمال علمه بها كأنها مبصرة عنده، ويقدر على الإشارة إليها،",
     "en": "The subtle point here is either an indication of his mastery of these meanings, such that, through the perfection of his knowledge of them, they became as if visible to him and he could point to them;"},
    {"type": "pair",
     "ar": "وإما الإشارة إلى كمال فطانة الطالب، إلى أن بلغ مبلغا صارت المعاني معه كالمبصرات عنده، واستحق أن يشار له إلى المعقول بالإشارة الحسية.",
     "en": "or an indication of the perfection of the student’s acumen, to the point that the meanings became for him like visible objects, so that he came to merit having the intelligible pointed out to him by a sensory demonstrative."},
    {"type": "pair",
     "ar": "وفي ذلك مبالغة في حث الطالب على تحصيل المعاني.",
     "en": "In this there is emphatic encouragement of the student to acquire the meanings."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جمع فائدة، وهو ما استفدت من علم أو مال أو جاه.",
     "en": "[Fawāʾid is] the plural of fāʾida (benefit), which is whatever one gains of knowledge, wealth, or standing."},
    {"type": "pair",
     "ar": "فاده المال يفيد، أي: ثبت له المال.",
     "en": "“The wealth accrued to him (fādahu al-māl yafīdu),” that is: the wealth became firmly established for him."},
    {"type": "pair",
     "ar": "فلك أن تريد بالفوائد الثوابت، يعني: هذه أمور ثابتة بعيدة عن البطلان.",
     "en": "So you may intend by “al-fawāʾid” the firmly-established things — meaning: these are settled matters, far removed from being void."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: كثيرة تامة، يقال: وفى الشيء وفيا على «فعول»، أي: كثر وتم.",
     "en": "That is: abundant and complete. One says “wafā al-shayʾu wufiyyan,” on the pattern faʿūl, meaning it became plentiful and complete."},
    {"type": "pair",
     "ar": "فقوله: «بحل» متعلق بـ«وافية» على تضمين معنى التعلق.",
     "en": "So his words “bi-ḥall” (in resolving) are governed by “wāfiya,” by implanting in it the sense of connection."},
    {"type": "pair",
     "ar": "ولك أن تجعل الوافية من «وفى بعهده» أي: لم يغدر.",
     "en": "You may also take “wāfiya” from “wafā bi-ʿahdihi” (he kept his covenant), that is: he did not betray."},
    {"type": "pair",
     "ar": "فقوله: «بحل» متعلق بالوافية، لكن الأول أبلغ وأتم معنى.",
     "en": "In that case “bi-ḥall” is governed by “wāfiya” [in this sense]; but the first is more eloquent and more complete in meaning."},
    {"type": "pair",
     "ar": "والفوائد: اسم لكتاب في المعاني، والوافية: اسم للمتوسط، والمشارق: اسم لكتاب في الحديث.",
     "en": "“Al-Fawāʾid” is the title of a book on rhetoric (maʿānī); “al-Wāfiya” is the title of an intermediate work; and “al-Mashāriq” is the title of a book on ḥadīth."},
    {"type": "pair",
     "ar": "وفي درج أسماء الكتب بلا شائبة تكلف مزيد تحسين للكلام البليغ.",
     "en": "In weaving in the titles of [these] books without a trace of artificiality there is a further embellishment of the eloquent discourse."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "والحل مصدر «حل» بمعنى فك، ومضارعه «يحل» بضم العين.",
     "en": "“Al-ḥall” is the verbal noun (maṣdar) of “ḥalla” in the sense of undoing/loosening, whose imperfect is “yaḥullu,” with a ḍamma on the middle radical (ʿayn)."},
    {"type": "pair",
     "ar": "وأما مضارع «حل» ضد حرم فبالكسر.",
     "en": "As for the imperfect of “ḥalla” meaning the opposite of “to be forbidden” (i.e., to be lawful), it is with a kasra."},
    {"type": "pair",
     "ar": "والذي بمعنى نزل ففي مضارعه وجهان.",
     "en": "And the one meaning “to alight/encamp” admits two possibilities in its imperfect."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المشكل: من الإشكال بمعنى الاشتباه.",
     "en": "“Al-mushkil” (the difficult) derives from “ishkāl,” meaning resemblance/ambiguity."},
    {"type": "pair",
     "ar": "وإنما سمي الحق الخفي مشكلا؛ لأنه يشبه الباطل.",
     "en": "The hidden truth is called “mushkil” only because it resembles the false."},
    {"type": "pair",
     "ar": "والتاء في «الكافية» للمبالغة، أو النقل من المعنى الوصفي إلى الاسمي، أو التأنيث باعتبار أن الكتاب رسالة.",
     "en": "The tāʾ in “al-Kāfiya” is for hyperbole, or for transferring [the word] from an adjectival to a nominal sense, or for feminine gender in view of the book’s being a “risāla” (treatise)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "صفة الكافية، أو حال منها.",
     "en": "[It is] an adjective of al-Kāfiya, or a circumstantial qualifier (ḥāl) of it."},
    {"type": "pair",
     "ar": "قوله: «للعلامة» تاؤه للمبالغة.",
     "en": "His words “lil-ʿallāma”: its tāʾ is for hyperbole."},
    {"type": "pair",
     "ar": "ولم يطلق على الله سبحانه، مع أنه الجدير بذلك، لمانع، وهو توهم التأنيث.",
     "en": "It is not applied to God, Glorified is He — although He is most worthy of it — because of an impediment, namely the false suggestion of feminine gender."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بكسر الهاء، ويجوز الفتح أيضا؛ لأنه جاء لازما ومتعديا.",
     "en": "With a kasra on the hāʾ; the fatḥa is also permissible, because it [the verb ishtahara] occurs both intransitively and transitively."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "هما كنايتان عن جميع الأرض والبلاد.",
     "en": "The two [the East and the West] are metonymies for the whole earth and all lands."},
    {"type": "pair",
     "ar": "وذلك لأن من عادة العرب ذكر طرفي الشيء وإرادة الجميع.",
     "en": "This is because it is the custom of the Arabs to mention the two extremes of a thing while intending the whole."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "وإعرابه: إما بالجر على البدلية عن العلامة، أو الرفع بتقدير: هو، أو النصب بتقدير: أعني.",
     "en": "Its case-inflection: either genitive, as a substitute (badal) for “al-ʿallāma”; or nominative, with an implied “he is”; or accusative, with an implied “I mean.”"},
    {"type": "pair",
     "ar": "فالجر أولى لعدم التقدير فيه.",
     "en": "The genitive is preferable, since it involves no ellipsis."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "عطف بيان للشيخ، وتابع له في الإعراب الثلاثة.",
     "en": "[It is] an explicative apposition (ʿaṭf bayān) to “al-Shaykh,” following it in [any of] the three case-endings."},
    {"type": "pair",
     "ar": "وهو كنية صاحب الكافية، واسمه عثمان.",
     "en": "It is the kunya of the author of al-Kāfiya, whose given name is ʿUthmān."},
    {"type": "pair",
     "ar": "وهمزته قطعية؛ إذ لا يراد منه المعنى الإضافي.",
     "en": "Its hamza is a disjunctive hamza (hamzat qaṭʿ), since the genitival sense [of “ibn”] is not intended here."},
]
