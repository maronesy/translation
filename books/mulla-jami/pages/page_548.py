# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 548 (printed ٥٤٧)."""

PAGE_NUMBER = 548
PRINTED_PAGE = "٥٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وواوها) أي: واو «رب» في حكمها» at the foot of PDF p. 547.
    {"type": "matn",
     "ar": "(تدخل على نكرة موصوفة) مثل:",
     "en": "(It enters upon a qualified indefinite noun), as in:"},
    {"type": "verse",
     "ar": "وبلدة[[١]] ليس بها أنيس          إلا اليعافير وإلا العيس",
     "en": "And many a land wherein there is no companion, save the gazelles and save the white camels."},
    {"type": "matn",
     "ar": "وهذه الواو للعطف عند سيبويه، وليست بجارة[[٢]].",
     "en": "This wāw is for coordination (ʿaṭf) according to Sībawayh, and does not govern the genitive."},
    {"type": "matn",
     "ar": "فإن لم تكن في أول الكلام، فكونها للعطف ظاهر، وإن كانت في أوله فيقدر له معطوف عليه.",
     "en": "If it is not at the beginning of the discourse, its being for coordination is evident; if it is at its beginning, something to which it is coordinated is supposed for it."},
    # REVIEW: «وعند الكوفيون» is printed (nominative after «عند»); grammatically «الكوفيين» is expected. Transcribed as printed.
    {"type": "matn",
     "ar": "وعند الكوفيون: أنها حرف عطف، ثم صارت قائمة مقام «رب» جارة بنفسها، لصيرورتها بمعنى «رب»[[٣]]،",
     "en": "According to the Kūfans, it is a particle of coordination which then came to stand in place of “rubba”, governing the genitive by itself, because it has come to bear the sense of “rubba”;"},
    {"type": "matn",
     "ar": "فلا يقدرون له معطوفا عليه، لأن ذلك تعسف[[٤]].",
     "en": "so they do not suppose for it anything to which it is coordinated, since that is far-fetched."},

    {"type": "section", "ar": "[واو القسم]",
     "en": "The Wāw of Oaths"},

    {"type": "matn",
     "ar": "(وواو القسم: إنما تكون عند حذف الفعل[[٥]]) أي: فعل القسم، فلا يقال: «أقسمت",
     "en": "(And the wāw of oaths occurs only when the verb is elided), that is, the verb of swearing; so one does not say “aqsamtu…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "البلدة: كل قطعة من الأرض مستحيزة عامرة أو غامرة.",
     "en": "Al-balda: any distinct tract of land, inhabited or desolate."},
    {"type": "pair",
     "ar": "والأنيس: الديك والمؤانس وكل مأنوس به.",
     "en": "Al-anīs: the cockerel, a companion, and anything with which one is at ease."},
    {"type": "pair",
     "ar": "واليعفور: ظبي بلون التراب أو عام ويضم الياء والخشف.",
     "en": "Al-yaʿfūr: a gazelle of the colour of dust, or [gazelles] in general; [the word is also read] with ḍamma on the yāʾ; and the fawn."},
    {"type": "pair",
     "ar": "والعيس: بالكسر الإبل البيض يخالط بياضها شقرة، كل ذلك من القاموس.",
     "en": "Al-ʿīs, with kasra: white camels whose whiteness is mixed with a reddish tinge. All of this is from al-Qāmūs."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بل الجارة «رب» المقدرة، ويحذف حرف الجر قياسا إذا كان «رب» بشرطين:",
     "en": "Rather, what governs the genitive is the implied “rubba”. A preposition is elided by analogy, when it is “rubba”, under two conditions:"},
    {"type": "pair",
     "ar": "أحدهما: أن يكون في الشعر خاصة.",
     "en": "First, that it be in poetry specifically."},
    {"type": "pair",
     "ar": "والثاني: بعد الواو، والفاء، أو بل. وأما حذفها بدون هذه الحروف فشاذ في الشعر أيضا، كذا في الرضي.",
     "en": "Second, [that it come] after wāw, fāʾ or bal. Its elision without these particles is anomalous even in poetry. So it is in al-Raḍī."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: «في وسط لكلام» is printed; «الكلام» is expected. Transcribed as printed.
    {"type": "pair",
     "ar": "بدليل أنه لا يجوز إظهار «رب» بعدها كما جاز بعد الفاء وبل،",
     "en": "The proof is that “rubba” may not be expressed after it, as it may after fāʾ and bal;"},
    {"type": "pair",
     "ar": "ومع ذلك لا يجوز دخول حرف العطف عليها في وسط لكلام اعتبارا لأصلها بخلاف واو القسم،",
     "en": "and despite this, a particle of coordination may not enter upon it in the middle of discourse, in consideration of its origin; unlike the wāw of oaths,"},
    {"type": "pair",
     "ar": "فإنها لم تكن في الأصل واو العطف، فلذلك جاز دخول حرف العطف عليها نحو: فوالله، ووالله، وثم والله، كذا في الرضي.",
     "en": "for it was not originally the wāw of coordination, and so a particle of coordination may enter upon it, as in “fa-wa-llāhi”, “wa-wa-llāhi” and “thumma wa-llāhi”. So it is in al-Raḍī."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وجوب ارتكابه للفاء، وبل يسهل ذلك، ويخرجه عن كونه تعسفا.",
     "en": "The necessity of resorting to it for fāʾ and bal eases that and removes it from being far-fetched."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فالمعنى: لا يكون مستعملا إلا عند حذف الفعل، ولا يكون مستعملا إلا لغير السؤال.",
     "en": "So the meaning is: it is used only when the verb is elided, and it is used only for other than a request."},
    {"type": "pair",
     "ar": "فقوله: «عند حذف الفعل» خبر «يكون». وقوله: «لغير السؤال» خبر ثان أو خبر لواو القسم،",
     "en": "His words “when the verb is elided” are the predicate of “yakūn”, and his words “for other than a request” are a second predicate, or a predicate of “the wāw of oaths”."},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون أحدهما متعلقا بـ«يكون»، والآخر خبرا، أو كلاهما متعلق به على أنها تامة،",
     "en": "It is not permissible for one of them to be attached to “yakūn” and the other to be the predicate, or for both to be attached to it, [taking] it as complete (tāmma);"},
    {"type": "pair",
     "ar": "وإلا لكان الجزء الأخير من الكلام مقصورا عليه، كما تقرر في «إنما»، فيكون المعنى ما يكون عند حذف الفعل إلا لغير السؤال،",
     "en": "otherwise the last part of the sentence would be that to which [the statement] is restricted, as is established for “innamā”, and the meaning would be: “it does not occur when the verb is elided except for other than a request”;"},
    {"type": "pair",
     "ar": "وذلك غير مقصور مع أنه يوهم أنها عند عدم حذف الفعل تكون للسؤال.",
     "en": "but that is not restricted, and moreover it would suggest that when the verb is not elided it is for a request."},
    {"type": "pair",
     "ar": "قال العصام: قوله: عند حذف الفعل خبر «تكون». وقوله: «لغير السؤال» خبر ثان،",
     "en": "Al-ʿIṣām said: his words “when the verb is elided” are the predicate of “takūn”, and his words “for other than a request” are a second predicate;"},
    {"type": "pair",
     "ar": "أي: لا تكون إلا عند حذف الفعل، ولا تكون إلا لغير السؤال،",
     "en": "that is, it occurs only when the verb is elided, and occurs only for other than a request."},
    {"type": "pair",
     "ar": "وليس أحدهما متعلقا بـ«تكون»، والآخر خبرا لفساد المعنى، فافهم.",
     "en": "One of them is not attached to “takūn” with the other as predicate, because the meaning would be corrupted. So understand."},
]
