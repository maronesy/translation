# -*- coding: utf-8 -*-
"""
Mulla Jami — al-Fawa'id al-Diya'iyya (commentary on al-Kafiya of Ibn al-Hajib)
Source page: 24 of the PDF  (printed page ٢٣) — the Commentator's Introduction.

Each block is one unit of content. Sentence pairs carry the Arabic ("ar")
with the English translation ("en") rendered directly beneath it.

Block types:
  section  – a titled section header (ar + en)
  basmala  – the ornamental basmala line
  matn     – a sentence of the base text (matn), ar + en
  note     – opens a numbered footnote (num + optional label)
  pair     – a sentence pair inside the current footnote, ar + en
  rule     – a decorative divider
"""

PAGE_NUMBER = 24          # PDF page
PRINTED_PAGE = "٢٣"       # page number printed in the book

BLOCKS = [
    {"type": "section", "ar": "[مقدمة الشارح]",
     "en": "The Commentator’s Introduction"},

    {"type": "basmala"},

    # ---------------- The base text (matn) ----------------
    {"type": "khutba",
     "ar": "الحمد[[١]] لوليه[[٢]]،",
     "en": "All praise belongs to the One who is worthy of it,"},
    {"type": "khutba",
     "ar": "والصلاة على نبيه[[٣]]،",
     "en": "and blessings be upon His Prophet,"},
    {"type": "khutba",
     "ar": "وعلى آله[[٤]] وأصحابه[[٥]] المتأدبين[[٦]] بآدابه[[٧]].",
     "en": "and upon his family and his companions, who are refined by his discipline (adab)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولا بد في مقام الحمد من خمسة أشياء:",
     "en": "In the setting of praise (ḥamd), five things are indispensable:"},
    {"type": "pair",
     "ar": "الحامد: هو المصنف، والمحمود: هو الله تعالى، والمحمود عليه: هو النعمة، والمحمود به: هو الألفاظ، والحمد: هو الأمر المعنوي بين الحامد والمحمود.",
     "en": "the praiser (al-ḥāmid) — he is the author; the Praised (al-maḥmūd) — He is Allah, the Exalted; that for which He is praised (al-maḥmūd ʿalayhi) — it is [His] blessing; that by which He is praised (al-maḥmūd bihi) — it is the words uttered; and praise itself (al-ḥamd) — it is the abstract reality standing between the praiser and the Praised."},
    {"type": "pair",
     "ar": "قوله: «الحمد» مصدر المعلوم، واللام للجنس أو الاستغراق، أي: كل حمد من الأزل إلى الأبد من أي حامد كان.",
     "en": "His words “al-ḥamd” form the verbal noun of the active voice; the definite article (lām) denotes the genus or all-inclusiveness (istighrāq) — that is: every praise, from pre-eternity to everlasting, from whatever praiser it may issue."},
    {"type": "pair",
     "ar": "ويحتمل أن يكون مصدر المجهول أو القدر المشترك بين المصدرين، فإن مقام حمده سبحانه يلائمه الاستيعاب كما يلائمه الاستغراق. ويحتمل أن يكون الحاصل بالمصدر.",
     "en": "It may also be the verbal noun of the passive voice, or the measure common to both verbal nouns — for the station of praising Him, Glorified is He, befits comprehensiveness (istīʿāb) just as it befits all-inclusiveness (istighrāq). It may likewise denote the result produced by the verbal action (al-ḥāṣil bi-l-maṣdar)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "اللام متعلق بالخبر. الإضافة في «لوليه» للاستغراق، والضمير البارز فيه راجع إلى الحمد.",
     "en": "The lām (in li-waliyyihi) is governed by the predicate. The genitive construction in “li-waliyyihi” denotes all-inclusiveness, and the visible pronoun within it refers back to “praise” (al-ḥamd)."},
    {"type": "pair",
     "ar": "قوله: «لوليه» أي: للحري بجنس الحمد.",
     "en": "His words “li-waliyyihi” [mean: to] the One most worthy of the genus of praise."},
    {"type": "pair",
     "ar": "لا يخفى ما في ترك التصريح باسمه سبحانه من التعظيم والإجلال وادعاء التعيين، وأن الوهم لا يذهب إلى أن الجدير بالحمد غيره تعالى،",
     "en": "It is not hidden what lies in refraining from naming Him explicitly, Glorified is He — magnification, reverence, and the tacit claim that His identity is self-evident; and [it conveys] that no supposition could stray to imagine the one deserving of praise to be other than Him, the Exalted;"},
    {"type": "pair",
     "ar": "وتعليق الحمد صريحا بما يشعر بالعلية، وغرابة الأسلوب التي تجلب الطباع إليه لكون الجديد لذيذا.",
     "en": "and [there is benefit] in attaching praise expressly to that which signals the underlying cause, and in the freshness of the modes of expression that draw dispositions toward it — since what is novel is delightful."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "خبر، والضمير البارز راجع إلى الولي، تقديره: على نبي ولي الحمد.",
     "en": "[It is] a predicate, and the visible pronoun refers back to “the Master” (al-waliyy); its implied sense is: “upon the Prophet of the Master of praise.”"},
    {"type": "pair",
     "ar": "قوله: «والصلاة على نبيه»: النبي إنسان بعثه الله تعالى إلى الخلق لتبليغ أحكامه.",
     "en": "His words “and blessings upon His Prophet”: the Prophet (nabī) is a human being whom Allah, the Exalted, has sent to creation to convey His rulings."},
    {"type": "pair",
     "ar": "والرسول أخص منه، وهو إنسان كذلك يكون له كتاب وشريعة.",
     "en": "The Messenger (rasūl) is more specific than he: he too is a human being, but one granted a Book and a sacred law (sharīʿa)."},
    {"type": "pair",
     "ar": "والأصل في الإضافة العهد الخارجي، فبهذا الأصل ينصرف إلى نبينا صلى الله عليه وسلم.",
     "en": "The default of the genitive construction is external, definite reference (al-ʿahd al-khārijī); by this default it points to our Prophet, may Allah bless him and grant him peace."},
    {"type": "pair",
     "ar": "وقد تكون للجنس والاستغراق، فيكون المعنى: والصلاة على كل نبي له تعالى.",
     "en": "It may, however, be generic and all-inclusive (istighrāq), so the sense becomes: “and blessings upon every prophet belonging to Him, the Exalted.”"},
    {"type": "pair",
     "ar": "فوجه اختياره على الرسول: إما بحسب اللفظ فلرعاية السجع، وإما بحسب المعنى.",
     "en": "The reason for his choosing it (the Prophet) over “the Messenger” is either with respect to wording — to preserve the rhymed prose (sajʿ) — or with respect to meaning."},
    {"type": "pair",
     "ar": "فعلى الثاني ظاهر؛ لأنه أشمل، وعلى الأول فللدلالة على أنه صلى الله تعالى عليه وسلم يستحق الصلاة بمرتبة النبوة. ويعلم منه أن استحقاقه بمرتبة الرسالة بطريق الأولى.",
     "en": "On the second [consideration] it is evident, because [prophethood] is more encompassing; while on the first, it is to indicate that he — may Allah bless him and grant him peace — merits the blessing by virtue of the rank of prophethood. And from this it is understood that his meriting it by virtue of the rank of messengership follows all the more fittingly (a fortiori)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: أهل بيته.",
     "en": "That is: the people of his household (ahl al-bayt)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "جمع صاحب كطاهر وأطهار، أو جمع صحب — بسكون الحاء — كنهر وأنهار، أو صحب — بكسر الحاء — كنمر وأنمار، مخفف صاحب،",
     "en": "[Aṣḥāb is] the plural of ṣāḥib, like ṭāhir → aṭhār; or the plural of ṣaḥb — with a quiescent ḥāʾ — like nahr → anhār; or of ṣaḥib — with a kasra on the ḥāʾ — like namir → anmār, [ṣaḥib being] a lightened form of ṣāḥib;"},
    {"type": "pair",
     "ar": "بناء على ما قيل: من أن «فاعلا» لا يجمع على أفعال.",
     "en": "this being based on what has been said: that a word of the pattern fāʿil is not pluralized on the pattern afʿāl."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "«المتأدبين» صفة للآل، والأصحاب على سبيل البدل، أو من عطف البيان والتفسير لإبهام ناشئ منه،",
     "en": "“Al-mutaʾaddibīn” (those refined) is an adjective qualifying “the family” (al-āl), while “the companions” is included by way of substitution (badal); or it comes by way of appositional explication (ʿaṭf al-bayān wa-l-tafsīr) to remove an ambiguity arising from it,"},
    {"type": "pair",
     "ar": "تقديره: وعلى آله المتأدبين وأصحابه المتأدبين.",
     "en": "its implied form being: “and upon his family who are refined and his companions who are refined.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "التزم أهل السنة بإدخال «علي» على الآل ردا على الشيعة، فإنهم منعوا ذكر «علي» بين النبي وآله،",
     "en": "The People of the Sunna are committed to including “ʿAlī” under [the heading of] “the Family” (āl), in refutation of the Shīʿa; for they forbade the mention of “ʿAlī” between the Prophet and his Family,"},
    {"type": "pair",
     "ar": "وينقلون في ذلك حديثا في الصحاح: آل الرجل أهله وعياله، وآله أيضا أتباعه.",
     "en": "and they cite in this regard a report. In al-Ṣiḥāḥ [it is said]: a man’s āl (family) are his household and dependents, and his āl are also his followers."},
    {"type": "pair",
     "ar": "هذا، ولو حمل على الثاني يكون ذكر الأصحاب تخصيصا بعد التعميم.",
     "en": "This being so, if [āl] is taken in the second sense [i.e., followers], then the mention of “the Companions” amounts to specification after generalization."},
    {"type": "pair",
     "ar": "وللفقهاء أقوال في تعيين آل الرسول، وهذا المقام لا يسعه.",
     "en": "The jurists hold various views on defining the āl of the Messenger, which this place cannot accommodate."},
    {"type": "pair",
     "ar": "في الصحاح: الأدب: أدب النفس وأدب الدرس.",
     "en": "In al-Ṣiḥāḥ: adab is [of two kinds] — the discipline of the self (adab al-nafs) and the discipline of instruction (adab al-dars)."},
    {"type": "pair",
     "ar": "ولا يخفى أن آله وأصحابه متأدبون بآداب نفسه وآداب درسه، وهو تبليغ الكتاب والأحكام.",
     "en": "It is not hidden that his Family and his companions are refined by the discipline of his self and the discipline of his teaching — which is the conveyance of the Book and the rulings."},
    {"type": "pair",
     "ar": "وفي ذكر الأدب براعة الاستهلال؛ لأن النحو من قسم الأدب.",
     "en": "And in the mention of adab lies “the excellence of the opening” (barāʿat al-istihlāl), for grammar (naḥw) belongs to the category of adab (letters)."},
]
