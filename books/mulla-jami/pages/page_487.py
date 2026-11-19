# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 487 (printed ٤٨٦)."""

PAGE_NUMBER = 487
PRINTED_PAGE = "٤٨٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لأن نون التأكيد لشدة الاتصال بمنزلة جزء الكلمة،» at the foot of PDF p. 486.
    {"type": "matn",
     "ar": "فلو دخل الإعراب قبلها يلزم دخوله في وسط الكلمة، ولو دخل عليها لزم دخوله على كلمة أخرى حقيقة،",
     "en": "…so if the inflection entered before it, its entering in the middle of the word would follow; and if it entered upon it, its entering upon what is really another word would follow;"},
    {"type": "matn",
     "ar": "ولأن نون جمع المؤنث في المضارع يقتضي أن يكون ما قبلها ساكنا لمشابهتها نون جمع المؤنث في الماضي، فلا يقبل الإعراب.",
     "en": "and because the nūn of the feminine plural in the muḍāriʿ requires that what precedes it be quiescent, owing to its resemblance to the nūn of the feminine plural in the past, so it does not admit inflection."},
    {"type": "matn",
     "ar": "(وإعرابه: رفع، ونصب) يشارك الاسم فيهما (وجزم) يختص به كالجر بالاسم.",
     "en": "(Its inflection is: the nominative (rafʿ) and the accusative (naṣb)), in which it shares with the noun, (and the jussive (jazm)), which is peculiar to it, as the genitive (jarr) is to the noun."},
    {"type": "matn",
     "ar": "(فالصحيح) منه[[١]] وهو عند النحاة[[٢]]: «ما لم يكن حرفه الأخير حرف علة»",
     "en": "(So the sound [verb]) of it, which among the grammarians is “that whose final letter is not a weak letter”,"},
    {"type": "matn",
     "ar": "(المجرد عن ضمير بارز مرفوع) متصل به (للتثنية[[٣]]) مذكرا كان أو مؤنثا، مثل: «يضربان، وتضربان».",
     "en": "(free of a visible nominative pronoun) joined to it (for the dual), whether masculine or feminine, as in “yaḍribāni” and “taḍribāni”,"},
    {"type": "matn",
     "ar": "(والجمع) المذكر مثل: «يضربون وتضربون».",
     "en": "(and the plural), masculine, as in “yaḍribūna” and “taḍribūna”,"},
    {"type": "matn",
     "ar": "والمؤنث[[٤]] مثل: «يضربن وتضربن».",
     "en": "and feminine, as in “yaḍribna” and “taḍribna”,"},
    {"type": "matn",
     "ar": "(والمخاطب المؤنث) مثل: «تضربين».",
     "en": "(and the feminine addressee), as in “taḍribīna”."},
    {"type": "matn",
     "ar": "فهذه أربع صيغ «يضرب» في الواحد الغائب المذكر، و«تضرب» في الموضعين: في الواحد الغائب المؤنث، والواحد المذكر المخاطب، و«أضرب» في المتكلم الواحد، و«نضرب» في المتكلم مع الغير",
     "en": "So these are four forms: “yaḍribu” in the absent masculine singular; “taḍribu” in two places, the absent feminine singular and the addressed masculine singular; “aḍribu” for the single speaker; and “naḍribu” for the speaker with another,"},
    {"type": "matn",
     "ar": "(بالضمة) في حال الرفع (والفتحة) في حال النصب (لفظا[[٥]]) أي: حال كون الضمة، والفتحة لفظيتين.",
     "en": "[are inflected] (with the ḍamma) in the state of the nominative, (and the fatḥa) in the state of the accusative, (overtly), that is, while the ḍamma and the fatḥa are pronounced."},
    {"type": "matn",
     "ar": "(والسكون) في حال الجزم، (مثل: «يضرب»[[٦]]، و«لن يضرب»، و«لم يضرب»).",
     "en": "(And with sukūn) in the state of the jussive, (as in “yaḍribu”, “lan yaḍriba” and “lam yaḍrib”)."},
    {"type": "matn",
     "ar": "(و) المضارع (المتصل به[[٧]] ذلك) أي: ذلك الضمير البارز المرفوع، وذلك في خمسة",
     "en": "(And) the muḍāriʿ (to which that is joined), that is, that visible nominative pronoun, and that is in five…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: من المضارع المعرب: وهو ما لم يتصل به نون تأكيد ولا نون جمع مؤنث.",
     "en": "That is, of the inflected muḍāriʿ, namely that to which neither a nūn of emphasis nor a nūn of the feminine plural is joined."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «احتراز عما هو أهل التصريف» (one would expect «عما هو عند أهل التصريف»); transcribed as printed.
    {"type": "pair",
     "ar": "احتراز عما هو أهل التصريف، وهو مستغن عن التعريف.",
     "en": "A precaution against what [it is among] the people of morphology (taṣrīf), and that needs no definition."},
    {"type": "pair",
     "ar": "وإنما قال: «حرفه الأخير»، ولم يقل: «لامه» ليشمل نحو: «يحمر» بلا شبهة.",
     "en": "He said “its final letter” and did not say “its lām” only so that it would include, without doubt, a case like “yaḥmarru”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا حاجة إلى ذكر هذه القيود؛ لأنه ليس ضمير بارز مرفوع متصل إلا للتثنية والجمع والمخاطب.",
     "en": "There is no need to mention these restrictions, because there is no visible, nominative, joined pronoun except for the dual, the plural and the addressee."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن الضمير البارز في الصحيح المعرب لا يكون لجمع المؤنث، فالجمع المطلق في هذا المقام ينصرف إلى المذكر",
     "en": "Against this: the visible pronoun in the inflected sound [verb] is not for the feminine plural, so the unqualified plural in this place refers to the masculine;"},
    {"type": "pair",
     "ar": "ولذلك صح قوله: فيما بعد والمتصل به ذلك بالنون وحذفها؛ إذ لو كان المشار إليه بذلك شاملا لضمير جمع المؤنث لانتقض الحكم لجمع المؤنث.",
     "en": "and for that reason his later words “and that to which that is joined, with the nūn and its omission” are valid; for if what is referred to by “that” included the pronoun of the feminine plural, the ruling would be broken for the feminine plural."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "حقيقة أو حكما، فإن الضمة والفتحة في حالة الوقف في حكم الملفوظ، ولذا يكون الوقف بالإشمام أو الروم والنقل،",
     "en": "Really or by status; for the ḍamma and the fatḥa in the state of pause have the status of what is pronounced, and for that reason the pause may be with ishmām (lip-rounding), or rawm (slight vocalization) and naql (transfer of the vowel);"},
    {"type": "pair",
     "ar": "وليستا تقديريتين على ما وهم، كما عرفت من معنى التقديري.",
     "en": "they are not suppositional (taqdīrī), as has been wrongly supposed, as you have learned from the meaning of “suppositional”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "مثال للصحيح المجرد عن ضمير بارز مرفوع لا لإعرابه حتى يكون قاصرا.",
     "en": "An example of the sound [verb] free of a visible nominative pronoun, not of its inflection, so that it would be deficient."},
    {"type": "pair",
     "ar": "والمتبادر من كلام الشارح أنه جعله مثالا للإعراب قائمة بما ألحق به.",
     "en": "What first comes to mind from the Commentator’s words is that he made it an example of the inflection, completed by what he appended to it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا يخفى أن الظاهر من سياق كلام المصنف أن قوله: والمتصل معطوف على المجرد، وهو مع ما يقابله تفصيل للصحيح،",
     "en": "It is not hidden that what is evident from the context of the author’s words is that his word “and the joined” is coordinated with “the free”, and that, together with what is set against it, it is a detailing of the sound [verb];"},
    {"type": "pair",
     "ar": "لكن الصحيح عطفه على الصحيح المجرد لا على مجرد المجرد، فنبه الشارح",
     "en": "but the correct view is that it is coordinated with “the sound, free [verb]”, not with “free” alone; so the Commentator drew attention…"},
]
