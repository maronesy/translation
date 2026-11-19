# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 39 (printed ٣٨)."""

PAGE_NUMBER = 39
PRINTED_PAGE = "٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "وقد أجيب عن الإشكالين[[١]]: بأنه ليس ههنا[[٢]] لفظ وضع بإزاء لفظ آخر مفردا كان أو مركبا[[٣]]، بل بإزاء مفهوم كلي أفراده ألفاظ، كلفظة الاسم، والفعل، والحرف، والخبر، والجملة، وغيرها.",
     "en": "The two difficulties have already been answered [thus]: there is here no expression posited to correspond to another expression — whether singular or compound — but rather [posited] to correspond to a universal concept (mafhūm kullī) whose individual instances are expressions, like the words “ism” (noun), “fiʿl” (verb), “ḥarf” (particle), “khabar” (predicate), “jumla” (sentence), and the like."},
    {"type": "matn",
     "ar": "ولا يخفى عليك أن هذا الحكم منقوض بأمثال الضمائر[[٤]] الراجعة إلى ألفاظ مخصوصة مفردة أو مركبة، فإن الوضع فيها[[٥]] وإن كان عاما[[٦]]، لكن الموضوع له خاص، فليس هناك مفهوم كلي هو الموضوع له في الحقيقة[[٧]].",
     "en": "It is not hidden from you that this ruling is refuted by such things as pronouns (ḍamāʾir) that refer back to particular expressions, whether singular or compound; for even though the positing in their case is general (ʿāmm), that which is posited-for is particular (khāṣṣ). Hence there is no universal concept that is, in reality, that which is posited-for."},
    {"type": "matn",
     "ar": "(مفرد) وهو:",
     "en": "His words “mufrad” (singular). It is:"},
    {"type": "matn",
     "ar": "١- إما مجرور على أنه صفة لـ«معنى»، ومعناه[[٨]] حينئذ: ما لا يدل لفظه على جزئه.",
     "en": "(1) either in the genitive, on the basis that it is an adjective qualifying “maʿnā” (a meaning), its sense in that case being: “that whose wording does not indicate a part of it”;"},
    {"type": "matn",
     "ar": "وفيه أنه يوهم أن اللفظ موضوع للمعنى المتصف بالإفراد والتركيب[[٩]]",
     "en": "but against this: it gives the false impression that the expression is posited for the meaning that is characterized by singularity (ifrād) and composition (tarkīb)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الإشكال الأول: وهو أنه قد وضع بعض الألفاظ بإزاء بعض آخر فكيف... إلى آخره.",
     "en": "The first difficulty: namely, that some expressions have been posited to correspond to certain others, so how…—to the end [of it]."},
    {"type": "pair",
     "ar": "الإشكال الثاني: وهو أنه قد وضع بعض الكلمات المفردة بإزاء الألفاظ المركبة إلى آخره.",
     "en": "The second difficulty: namely, that some singular words have been posited to correspond to compound expressions—to the end [of it]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: فيما بين الألفاظ المستعملة في مقام الحكم على اللفظ. وقيل: في مقام نقض تعريف الكلمة.",
     "en": "That is: among the expressions used in the context of predicating something of the wording. And it is said: in the context of refuting the definition of the “word” (kalima)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صرح بذلك ليتحقق مادة الإشكال الثاني أيضا. فالعطف بالواو أنسب لهذا الغرض، إلا أن يقال: ذكر «أو» بملاحظة إرجاع الضمير باعتبار أصل التحقق.",
     "en": "He stated this explicitly so that the substance of the second difficulty too might be realized. Coordination by the wāw (“and”) would be more suitable for this purpose — unless one says: “or” was mentioned in view of the referring-back of the pronoun, taking into account the basic [fact of] realization."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: تلك الضمائر.",
     "en": "That is: those pronouns."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الضمير المجرور — أعني «فيها» — إن كان راجعا إلى الضمائر، فقوله: «وإن كان عاما» حينئذ بيان للواقع، وإشارة إلى أن الوضع فيها لو فرض أنه ليس بعام، فهو أولى بأن لا يكون هناك مفهوم كلي.",
     "en": "The genitive pronoun — I mean “fīhā” (in their case) — if it refers back to the pronouns, then his words “even though it is general” are, in that case, a statement of the actual situation, and an indication that, if the positing in their case were supposed not to be general, it would be all the more fitting that there be no universal concept there."},
    {"type": "pair",
     "ar": "وإن كان راجعا إلى أمثال الضمائر، فقوله: «وإن كان عاما» إشارة إلى ما ليس الوضع فيه بعام، فإنه أولى بهذا الحكم، مثل أسماء حروف التهجي والسور والكتب.",
     "en": "But if it refers back to the likes of pronouns, then his words “even though it is general” are an indication of that in which the positing is not general — for such is [even] more fitting for this ruling — like the names of the spelling-letters (ḥurūf al-tahajjī), the [Qurʾānic] sūras, and the books."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: في مقام رجع الضمائر إلى الألفاظ المخصوصة، أو في مقام وضع أمثال الضمائر بإزاء الألفاظ المخصوصة.",
     "en": "That is: in the context of the pronouns’ referring back to particular expressions, or in the context of positing the likes of pronouns to correspond to particular expressions."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيد الموضوع له بقوله: «في الحقيقة»؛ لأنه هناك مفهوم كلي يجعلونه الموضوع له مجازا، فيقولون: ضمير الغائب موضوع لما تقدم ذكره، فيجعلون مفهوم ما تقدم ذكره موضوعا له مجازا.",
     "en": "He qualified “that which is posited-for” with his words “in reality,” because there is [in these cases] a universal concept which they treat as that which is posited-for [only] figuratively (majāzan); for they say: “the third-person pronoun is posited for that whose mention has preceded,” thus treating the concept of “that whose mention has preceded” as that which is posited-for figuratively."},
    {"type": "pair",
     "ar": "والمراد أنه موضوع لجزئيات هذا المفهوم.",
     "en": "What is [really] meant is that it is posited for the particular instances of this concept."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وفي معناه احتمالات: الأول: معنى المفرد المذكور. والثاني: معنى الموصوف بالمفرد. والثالث: أن يكون المراد من المعنى ما هو المذكور في المتن، والضمير للمفرد، فتأمل.",
     "en": "Concerning its sense there are [several] possibilities: the first, the sense of the aforementioned “mufrad” (singular); the second, the sense of that which is qualified by “mufrad”; the third, that what is meant by “the meaning” is what is mentioned in the base text (matn), and the pronoun refers to “mufrad” — so ponder [this]."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وذلك لأنك إذا عبرت عن شيء بما فيه معنى الوصفية، وعلقت به معنى مصدريا — إما في صيغة فعل أو غيرها — فهم منه في عرف اللغة أن ذلك الشيء موصوف بتلك الصفة حال تعلق ذلك المعنى به لا",
     "en": "That is because, when you express a thing by that which has in it an adjectival sense (maʿnā al-waṣfiyya), and you attach to it a verbal-noun sense — whether in the form of a verb or otherwise — it is understood therefrom, in the convention of the language, that that thing is qualified by that attribute at the time of that meaning’s attaching to it, not…"},
]
