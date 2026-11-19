# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 555 (printed ٥٥٤)."""

PAGE_NUMBER = 555
PRINTED_PAGE = "٥٥٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the Kāfiya sentence «(لها) ... (صدر الكلام)» on PDF p. 554.
    {"type": "matn",
     "ar": "(سوى «أن») المفتوحة (فهي بعكسها) أي: بعكس باقيها على حذف المضاف[[١]]، بأن يقتضي عدم الصدارة؛",
     "en": "…(except “anna”) with fatḥa, (for it is the reverse of them), that is, the reverse of the rest of them, with the first term of annexation elided, in that it requires not being at the head;"},
    {"type": "matn",
     "ar": "لأنها مع اسمها وخبرها في تأويل المفرد، فلا بد لها من التعلق بشيء آخر حتى يتم كلاما،",
     "en": "because it, together with its noun and its predicate, is interpreted as a single term, so it must be attached to something else for it to become complete speech;"},
    {"type": "matn",
     "ar": "وحينئذ لو وقعت في الصدر اشتبهت بـ«إن» المكسورة في صورة الكتابة.",
     "en": "and in that case, were it to occur at the head, it would be confused with “inna” with kasra in written form."},
    {"type": "matn",
     "ar": "وإنما حملنا العكس على اقتضاء عدم الصدارة، لا على عدم اقتضاء الصدارة؛ لأن مجرد الاستثناء[[٢]] يكفي في ذلك.",
     "en": "We took “the reverse” to mean requiring not being at the head, not merely not requiring the head, only because the exception alone suffices for that."},
    {"type": "matn",
     "ar": "(وتلحقها) أي: هذه الحروف (ما) الكافة (فتلغى[[٣]]) أي: تعزل هذه الحروف[[٤]] عن العمل لمكان «ما» الكافة[[٥]]",
     "en": "(And “mā” attaches to them), that is, to these particles — the restraining (kāffa) mā — (so they are cancelled), that is, these particles are removed from governing on account of the restraining “mā”,"},
    {"type": "matn",
     "ar": "(على الأفصح) أي: على أفصح اللغات، مثل: «إنما زيد قائم».",
     "en": "(according to the most eloquent [usage]), that is, according to the most eloquent of the dialects, as in “innamā Zaydun qāʾimun” (Zayd is only standing)."},
    {"type": "matn",
     "ar": "وقد تعمل على غير الأفصح، كما وقع في بعض أشعارهم[[٦]].",
     "en": "They sometimes govern according to the less eloquent [usage], as has occurred in some of their poetry."},
    {"type": "matn",
     "ar": "(وتدخل) هذه الحروف (حينئذ) أي: حين إذ يلحقها «ما» (على الأفعال)؛ لأن «ما»",
     "en": "(And then) — that is, when “mā” attaches to them — these particles (enter upon verbs), because “mā”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كيلا يلزم كون أن المفتوحة بعكس نفسها لدخولها في المرجع.",
     "en": "So that it would not follow that “anna” with fatḥa is the reverse of itself, since it is included in the referent [of the pronoun]."},
    {"type": "pair",
     "ar": "وإنما لم يرجع الضمير إلى ما بقي بعد الاستثناء رعاية للسابق واللاحق، فإن الضمير فيهما راجع إلى الحروف كلها.",
     "en": "He did not refer the pronoun to what remains after the exception only to keep in line with what precedes and what follows, for the pronoun in both refers to all the particles."},
    {"type": "pair",
     "ar": "قال العصام: كأنه ارتكب حذف المضاف لحفظ مماثلة ضميري لها وعكسها في المرجع،",
     "en": "Al-ʿIṣām said: it seems he resorted to eliding the first term of annexation to preserve the sameness of referent of the two pronouns in “lahā” and “bi-ʿaksihā”;"},
    {"type": "pair",
     "ar": "وإلا فيمكن رجوع ضمير عكسها إلى ما بقي بعد استثناء أن من هذه الحروف.",
     "en": "otherwise, the pronoun of “ʿaksihā” could refer to what remains of these particles after excepting “anna”."},
    {"type": "pair",
     "ar": "فإن قلت: إن أريد أن لهذه الحروف صدر الكلام وقعت فيه إن أيضا كذلك،",
     "en": "If you say: if it is meant that these particles have the head of the speech in which they occur, then “anna” is likewise;"},
    {"type": "pair",
     "ar": "وإن أريد لها صدر الكلام المقصود لذاته، فما ذكر من الموجب لا يوجبه؛",
     "en": "and if it is meant that they have the head of the speech intended for its own sake, then the cause mentioned does not necessitate it,"},
    {"type": "pair",
     "ar": "إذ الدلالة على قسم من الكلام لا يوجب إلا وقوعه في صدر كلامه؛ إذ لا ينكر صحة زيد أقائم أبوه؟",
     "en": "since indicating a kind of speech necessitates only its occurring at the head of its own speech; for the soundness of “Zaydun a-qāʾimun abūhu?” (Zayd — is his father standing?) is not denied."},
    {"type": "pair",
     "ar": "قلت: إن أريد أن لها صدر الكلام سواء كان مقصودا لذاته أو لا، واسم إن وخبرها ليسا كلاما، بل جعلا مفردا، فهي ليست في صدر الكلام وقعت فيه.",
     "en": "I say: it is meant that they have the head of the speech, whether intended for its own sake or not; and the noun and predicate of “anna” are not speech but have been made a single term, so it is not at the head of the speech in which it occurs."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيكون قوله: فهي بعكسها إعادة.",
     "en": "So his words “for it is the reverse of them” would be a repetition."},
    {"type": "pair",
     "ar": "والأصل في الكلام الإفادة، فلذلك حملناه على اقتضاء عدم الصدارة.",
     "en": "The default in speech is to convey [new] information; therefore we took it to mean requiring not being at the head."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "على الأفصح سمع العمل في «ليتما»، وقس عليه غيره.",
     "en": "On “according to the most eloquent”: governing has been heard in “laytamā”, and others were analogized to it."},
    {"type": "pair",
     "ar": "وبعضهم جعل «ما» الكافة اسما مبهما كضمير الشأن اسما لهذه الحروف والجملة بعدها خبرا،",
     "en": "Some made the restraining “mā” an indeterminate noun, like the pronoun of the matter (ḍamīr al-shaʾn), serving as the noun of these particles, with the sentence after it as the predicate;"},
    {"type": "pair",
     "ar": "والأصح أنها حرف زائد، كما في حالة إعمال «ليتما» وغيره بالاتفاق.",
     "en": "the sounder view is that it is a redundant particle, as it is, by agreement, when “laytamā” and the others govern."},
    {"type": "pair",
     "ar": "فلو قال: فتلغى على الأفصح والأصح لكان أنفع.",
     "en": "Had he said “so they are cancelled according to the most eloquent and the soundest [view]”, it would have been more useful."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "صرح بالمرجع لئلا يتوهم رجوع الضمير إلى إن أو ما سوى إن.",
     "en": "He stated the referent explicitly lest the pronoun be imagined to refer to “anna” or to what is other than “anna”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "عند الجمهور قدر الصفة لتصح سببية لحوق ما للإلغاء، وتقييد دخولها على الفعل، كما يشير تعليل الشارح للحكمين،",
     "en": "According to the majority. He supplied the adjective [“restraining”] so that the attachment of “mā” may properly be the cause of cancellation, and of the restriction of their entering upon the verb, as the commentator’s explanation of the two rulings indicates;"},
    {"type": "pair",
     "ar": "وما الكافة قسم من الزائد على ما في المغني: أن الزائدة نوعان أي: كافة وغير كافة.",
     "en": "and the restraining “mā” is a kind of the redundant [mā], according to what is in al-Mughnī: that the redundant [mā] is of two types, restraining and non-restraining."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يشعر بأن السماع يساعد في الجميع. وقد عرفت أنه مختص بـ«ليت».",
     "en": "This suggests that attested usage (samāʿ) supports [it] in all of them, whereas you have learned that it is restricted to “layta”."},
]
