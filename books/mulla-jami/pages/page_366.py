# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 366 (printed ٣٦٥)."""

PAGE_NUMBER = 366
PRINTED_PAGE = "٣٦٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «…ليثبت الحكم في صورة اللبس بالطريق الأولى.» at the foot of PDF p. 365 (new sentence).
    {"type": "matn",
     "ar": "(وإذا اجتمع ضميران[[١]]، وليس أحدهما مرفوعا) احترازا عن نحو: «أكرمتك»؛ إذ المرفوع كالجزء من الفعل، فكأنه لم يتحقق الفصل بين الفعل والضمير الثاني أصلا، فيجب اتصاله.",
     "en": "(When two pronouns come together and neither of them is nominative) — this excludes such as “akramtuka” (I honoured you), for the nominative is like part of the verb, so it is as if no separation at all had occurred between the verb and the second pronoun, and its connection is therefore obligatory —"},
    # REVIEW: «إجتماعهما» is printed with hamza under the alif (expected «اجتماعهما»); transcribed as printed.
    {"type": "matn",
     "ar": "(فإن كان) على تقدير إجتماعهما، وعدم كون أحدهما مرفوعا (أحدهما) أي: أحد الضميرين (أعرف) من الآخر،",
     "en": "(if), on the supposition of their coming together and neither of them being nominative, (one of them), that is, one of the two pronouns, (is more definite) than the other —"},
    {"type": "matn",
     "ar": "احتراز عما إذا تساويا[[٢]] نحو: «أعطاها إياه» حيث يجب الانفصال في الثاني، للتحرز عن تقدم أحد المتساويين من غير مرجح[[٣]]",
     "en": "this excludes the case where they are equal, as in “aʿṭāhā iyyāhu” (he gave her it), where separation is obligatory in the second, to avoid one of two equals preceding without a preponderating factor —"},
    {"type": "matn",
     "ar": "(وقدمته) أي: أحد الضميرين الذي هو أعرف على الآخر احتراز عما إذا كان الأعرف مؤخرا نحو: «أعطيته إياك»،",
     "en": "(and you have placed it first), that is, the one of the two pronouns that is more definite, before the other — this excludes the case where the more definite comes last, as in “aʿṭaytuhu iyyāka” (I gave him to you),"},
    {"type": "matn",
     "ar": "فيلزم انفصاله ليعذر[[٤]] المتكلم في تأخير الأعرف، ولا يلحقه طعن في أول الوهلة بإيراده على خلاف الأصل،",
     "en": "where its separation is required so that the speaker is excused for placing the more definite last, and incurs no reproach at first glance for using it contrary to the norm."},
    {"type": "matn",
     "ar": "وحكى سيبويه[[٥]] تجويز الاتصال أيضا نحو: «أعطيتهوك»",
     "en": "Sībawayh reported that connection is also allowed, as in “aʿṭaytuhūka”."},
    # REVIEW: the first «إن شئت أوردته منفصلا» before «أعطيتكه» would be expected to read «متصلا» (the example is connected, and the next clause gives the separate option); transcribed as printed.
    {"type": "matn",
     "ar": "(فلك الخيار[[٦]]) أي: الاختيار (في) الضمير (الثاني) إن شئت أوردته منفصلا (مثل: «أعطيتكه») باعتبار عدم الاعتداد[[٧]] بالفصل بما هو متصل،",
     "en": "(then you have the choice), that is, the option, (in) the (second) pronoun: if you wish, you use it separate [as printed] — (such as “aʿṭaytukahu”) (I gave it to you) — on the view that separation by what is connected is not taken into account;"},
    {"type": "matn",
     "ar": "وإن شئت أوردته منفصلا[[٨]] نحو: «أعطيتك إياه» باعتبار الاعتداد بالفصل بما يفصله، وإن كان متصلا",
     "en": "and if you wish, you use it separate, as in “aʿṭaytuka iyyāhu”, on the view that separation by what separates it is taken into account, even if it is connected."},
    {"type": "matn",
     "ar": "(و) نحو («ضربيك») فإنه اجتمع فيه ضميران ليس أحدهما مرفوعا لجر الأول بالإضافة، ونصب الثاني بالمفعولية، وقدم الأعرف الذي هو ضمير المتكلم،",
     "en": "(And) such as (“ḍarbīka”) (my striking you): two pronouns come together in it, neither of them nominative, since the first is genitive by annexation and the second accusative as object, and the more definite, the pronoun of the speaker, is placed first."},
    {"type": "matn",
     "ar": "فلك الوصل باعتبار عدم الاعتداد بالفصل بالمتصل ولك الفصل نحو: «ضربي إياك» للاعتداد بالفصل.",
     "en": "So you may connect, on the view that separation by the connected [pronoun] is not taken into account, and you may separate, as in “ḍarbī iyyāka”, on the view that the separation is taken into account."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولم يكن مما تعذر فيه الاتصال.",
     "en": "And it is not among the cases in which connection is impossible."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال سيبويه: إن كانا غائبين جاز الاتصال، وهو عربي، لكن الانفصال أكثر،",
     "en": "Sībawayh said: if both are third-person, connection is permitted and is [sound] Arabic, but separation is more frequent;"},
    {"type": "pair",
     "ar": "وإن لم يكونا غائبين لم يجز الاتصال. وأجاز المبرد قياسا على الغائب.",
     "en": "if they are not both third-person, connection is not permitted. Al-Mubarrad allowed it by analogy with the third person."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أنه يجوز أن يترجح الأول بأنه فاعل في الأصل كـ«ضربتك»، أو فاعل بحسب المعنى كالمفعول الأول من باب «أعطيت».",
     "en": "Against this: the first may be given preference because it is originally an agent, as in “ḍarabtuka”, or an agent in meaning, like the first object in the category of “aʿṭaytu”."},
    {"type": "pair",
     "ar": "ويمكن أن يدفع بأن الترجيح بالفاعلية ترجيح في المعنى لا في اللفظ، ووجوب الانفصال باعتبار البشاعة في اللفظ.",
     "en": "This can be answered: preference through agency is preference in meaning, not in wording, whereas the obligatory separation is on account of ugliness in the wording."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولأن الثاني أشرف من الأول لكونه أعرف، فيأنف من كونه متعلقا بما هو أدنى.",
     "en": "And because the second is nobler than the first, being more definite, so it disdains being attached to what is lower."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: عن النحاة. وقال: إنما هو شيء قاسوه، ولم يتكلم به العرب، فوضعوا الحروف غير موضعها، واستجاد المبرد مذهب النحاة.",
     "en": "That is, from the grammarians. He said: it is only something they derived by analogy, which the Arabs did not speak, so they put the letters out of their proper place. Al-Mubarrad approved the grammarians’ position."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لاجتماع جهتي الاتصال والانفصال.",
     "en": "Because the grounds for both connection and separation are present together."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو بسبب أن لا منقصة في التعلق مما هو أشرف منه، وصيرورته من جملته بالاتصال.",
     "en": "Or because there is no demeaning in being attached to what is nobler than it, and in its becoming part of it through connection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: «في باب «أعلمت»» printed; the comparison later in the note is with «علمت», so «علمت» may be intended; transcribed as printed.
    {"type": "pair",
     "ar": "قال الشيخ الرضي: والانفصال في باب «أعلمت» أولى من الانفصال في باب «أعطيت»؛",
     "en": "Shaykh al-Raḍī said: separation in the category of “aʿlamtu” is preferable to separation in the category of “aʿṭaytu”,"},
    {"type": "pair",
     "ar": "لأن المفعول الأول في باب «أعطيت» فاعل من حيث المعنى، فكان الثاني اتصل بضمير الفاعل، وفي مفعول باب «علمت» رائحة المبتدأ والخبر، وفيهما الانفصال.",
     "en": "because the first object in the category of “aʿṭaytu” is an agent in meaning, so the second is as if joined to an agent pronoun; whereas in the objects of the category of “ʿalimtu” there is a trace of the subject and predicate, and in those two there is separation."},
]
