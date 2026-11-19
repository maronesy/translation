# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 47 (printed ٤٦)."""

PAGE_NUMBER = 47
PRINTED_PAGE = "٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "كل واحدة من الكلمتين، فلا يلزم اتحادهما[[١]].",
     "en": "each one of the two words, so their being one and the same is not entailed."},
    {"type": "matn",
     "ar": "(بالإسناد) أي: تضمنا حاصلا بسبب إسناد[[٢]] إحدى الكلمتين إلى الأخرى.",
     "en": "His words “by predication (bi-l-isnād)” mean: a comprising that comes about by reason of the predication (isnād) of one of the two words to the other."},
    {"type": "matn",
     "ar": "والإسناد: نسبة إحدى الكلمتين[[٣]] حقيقة أو حكما[[٤]] إلى الأخرى، بحيث يفيد المخاطب فائدة[[٥]] تامة يصح السكوت عليها[[٦]].",
     "en": "And predication (isnād) is: the relating of one of the two words — whether in reality or in ruling (ḥukman) — to the other, in such a way that it conveys to the addressee a complete benefit (fāʾida) upon which it is sound to remain silent."},
    {"type": "matn",
     "ar": "فقوله: لفظ «ما» يتناول المهملات، والمفردات، والمركبات الكلامية والغير الكلامية.",
     "en": "So his words: the expression “mā (whatever)” takes in the meaningless utterances (al-muhmalāt), the single words (al-mufradāt), and the compounds — both the sentential (kalāmiyya) and the non-sentential."},
    {"type": "matn",
     "ar": "وبقيد «تضمن كلمتين» خرجت المهملات[[٧]] والمفردات.",
     "en": "And by the restriction “it comprises two words,” the meaningless utterances and the single words are excluded."},
    {"type": "matn",
     "ar": "وبقيد «الإسناد» خرجت المركبات الغير الكلامية، مثل: «غلام زيد»، و«رجل فاضل».",
     "en": "And by the restriction “predication,” the non-sentential compounds are excluded, such as “Zayd’s servant (ghulāmu Zaydin)” and “a virtuous man (rajulin fāḍilin).”"},
    {"type": "matn",
     "ar": "وبقيت المركبات الكلامية، سواء كانت خبرية[[٨]]، مثل: «ضرب زيد»، و«ضربت",
     "en": "And there remain the sentential compounds, whether they be declarative (khabariyya), such as “Zayd struck (ḍaraba Zaydun)” and “she struck (ḍarabat…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المتضمن والمتضمن في تضمن الكل لكل جزء.",
     "en": "That is: the container and the contained, in the containing of the whole for each of its parts."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لو جعلت الهيئة جزءا للكلام كان لتضمن الكلام للكلمتين معنى واضح لا يحتاج إلى هذا التدقيق، ولم يلتفت لاحتياجه إلى تصحيح كون الهيئة التي ليست بلفظ جزءا من اللفظ.",
     "en": "It is not hidden that, had the form (hayʾa) been made a part of the speech, the speech’s comprising the two words would carry a clear sense not requiring this fine precision; but no regard was paid to the need this entails — to establish that the form, which is not itself an utterance, is a part of the utterance."},
    {"type": "pair",
     "ar": "ولو جعل المتضمن — بالكسر — مجموع الكلمتين، والإسناد كما قيل، فإطلاق اللفظ عليه يحتاج إلى تأويل؛ إذ الإسناد ليس بلفظ.",
     "en": "And were “the container” (read with kasra: al-mutaḍammin) taken to be the totality of the two words together with the predication, as has been said, then applying the term “utterance” to it would require interpretation, since predication is not an utterance."},
    {"type": "pair",
     "ar": "وأيضا الإسناد ليس بجزء للكلام، فإنه إن أريد به نسبة أحد الأمرين إلى آخر، فهو مفهوم الكلام، وإن أريد منه ضم كلمة إلى أخرى، فهو صفة لأجزائه، فتأمل.",
     "en": "Furthermore, predication is not a part of the speech: for if by it is meant the relating of one of the two things to the other, then it is the very concept of the speech; and if by it is meant the adjoining of one word to another, then it is an attribute of its parts. So ponder this."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ويجوز أن يكون الباء للإلصاق، أي: تضمنا ملصقا بالإسناد.",
     "en": "It is permissible that the bāʾ [in bi-l-isnād] be for adhesion (ilṣāq), that is: a comprising joined to the predication."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أو ضم إحدى الكلمتين، أو نسبة مدلول إحدى الكلمتين.",
     "en": "Or: the adjoining of one of the two words, or the relating of the signification of one of the two words."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الكلمة الحكمية ما يصح وقوع مفرد موقعه.",
     "en": "The “word-in-ruling” (al-kalima al-ḥukmiyya) is that in whose place it is valid for a single word to occur."},
    {"type": "pair",
     "ar": "لا يقال: يخرج عن الإسناد الذي في الجملة الشرطية؛ لأن الشرط قيد للجزاء على زعم المصنف وزعمهم، ولذا قالوا: إن الإسناد إليه من خواص الاسم.",
     "en": "Let it not be said: [predication] falls outside the predication found in the conditional sentence, because the protasis (sharṭ) is a restriction (qayd) upon the apodosis (jazāʾ) according to the author and to their supposition — and for this reason they said that predication to it is among the peculiar properties of the noun."},
    {"type": "pair",
     "ar": "وقال: لا يأتي ذلك إلا في اسمين أو في فعل واسم.",
     "en": "And he said: “that occurs only in two nouns, or in a verb and a noun.”"},
    {"type": "pair",
     "ar": "ولو جعل الرابط بين الشرط والجزاء كما حققه السيد لخرج عنه قطعا؛ إذ لا يصح التعبير عن الشرطية بمفرد.",
     "en": "And were the connective (rābiṭ) between protasis and apodosis taken into account, as al-Sayyid has verified, it would certainly be excluded from it, since it is not valid to express the conditional by a single word."},
    {"type": "pair",
     "ar": "والدليل على أن الرابط بينهما صدق قولك: إن «ضربتني ضربتك»، وإن لم يوجد منك ضرب المخاطب.",
     "en": "The proof that there is a connective between the two is the truth of your statement, “if you strike me, I strike you,” even though no striking of the addressee has actually issued from you."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: من شأنه أن يقصد به إفادة المخاطب فائدة يصح السكوت عليها، أي: لو سكت المتكلم عليها لم يكن لأهل العرف مجال تخطئته ونسبته إلى القصور في باب الفائدة.",
     "en": "That is: it is of its nature that conveying to the addressee a benefit upon which silence is sound be intended by it — that is, were the speaker to fall silent upon it, the people of [linguistic] convention would have no room to fault him or to attribute deficiency to him in the matter of conveyed benefit."},
    {"type": "pair",
     "ar": "فدخل فيه إسناد الجملة الواقعة خبرا أو صفة أو صلة، ودخل أيضا إسناد الجملة التي علم مضمونها المخاطب.",
     "en": "So there enters under it the predication of a sentence occurring as a predicate (khabar), an adjective (ṣifa), or a relative clause (ṣila); and there also enters the predication of a sentence whose content the addressee already knows."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "صفة كاشفة للفائدة.",
     "en": "An explicative attribute (ṣifa kāshifa) qualifying “benefit.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الصرفة. وأما المركب من كلمتين ومهمل، فلا يخرج.",
     "en": "The purely [meaningless] ones. As for what is compounded of two words and a meaningless one, it is not excluded."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: محكية بها عن الواقع.",
     "en": "That is: [statements] by which reality is reported."},
]
